import csv
import json
import os

# --- Configuration ---
INPUT_FILE = 'health/medical_records/dna_raw.csv'
OUTPUT_JSON = 'health/dna_analysis.json'
OUTPUT_MD = 'health/dna_summary.md'

# --- SNP Definitions & Interpretation Logic ---
# Key: rsid
# Value: Dict with Name, Gene, Description, Allele Interpretation
# Note: Alleles are often reported on forward strand, but can vary.
# We will use simple "contains risk allele" logic or exact genotype mapping where possible.

SNP_DB = {
    # 1. METHYLATION
    'rs1801133': {
        'gene': 'MTHFR',
        'name': 'C677T',
        'type': 'Methylation',
        'risk_allele': 'A',  # Often reported as A or T. C is normal.
        'interpretations': {
            'GG': {'status': 'Normal', 'risk': 'Low', 'desc': 'Metabolismo normal de folato.'},
            'AG': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Redução de ~30-40% na eficiência. Suplementar B9 metilado.'},
            'GA': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Redução de ~30-40% na eficiência. Suplementar B9 metilado.'},
            'AA': {'status': 'Homozygous Risk', 'risk': 'High', 'desc': 'Redução de ~60-70% na eficiência. Risco elevado de homocisteína alta. B9/B12 metilados essenciais.'},
            'TT': {'status': 'Homozygous Risk', 'risk': 'High', 'desc': 'Redução de ~60-70% na eficiência. Risco elevado de homocisteína alta. B9/B12 metilados essenciais.'}, # T is the risk on some arrays
            'GT': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Redução de ~30-40% na eficiência.'},
            'TG': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Redução de ~30-40% na eficiência.'},
        }
    },
    'rs1801131': {
        'gene': 'MTHFR',
        'name': 'A1298C',
        'type': 'Methylation',
        'risk_allele': 'G', # Or C. A is normal (or T).
        'interpretations': {
            'TT': {'status': 'Normal', 'risk': 'Low', 'desc': 'Metabolismo normal.'},
            'AA': {'status': 'Normal', 'risk': 'Low', 'desc': 'Metabolismo normal.'},
            'TG': {'status': 'Heterozygous', 'risk': 'Low/Medium', 'desc': 'Leve redução na eficiência.'},
            'GT': {'status': 'Heterozygous', 'risk': 'Low/Medium', 'desc': 'Leve redução na eficiência.'},
            'AC': {'status': 'Heterozygous', 'risk': 'Low/Medium', 'desc': 'Leve redução na eficiência.'},
            'CA': {'status': 'Heterozygous', 'risk': 'Low/Medium', 'desc': 'Leve redução na eficiência.'},
            'GG': {'status': 'Homozygous Risk', 'risk': 'Medium', 'desc': 'Redução moderada na eficiência.'},
            'CC': {'status': 'Homozygous Risk', 'risk': 'Medium', 'desc': 'Redução moderada na eficiência.'},
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'Val158Met',
        'type': 'Methylation',
        'interpretations': {
            'GG': {'status': 'Warrior (Fast)', 'risk': 'Variable', 'desc': 'Degradação rápida de dopamina. Lida bem com stress, mas menor foco/memória. Risco de baixos níveis de estrogénio.'},
            'AA': {'status': 'Worrier (Slow)', 'risk': 'Variable', 'desc': 'Degradação lenta. Mais dopamina (foco, ansiedade). Sensível ao stress. Risco de acumulação de estrogénios.'},
            'AG': {'status': 'Warrior/Worrier', 'risk': 'Balanced', 'desc': 'Equilíbrio entre estabilidade emocional e foco.'},
            'GA': {'status': 'Warrior/Worrier', 'risk': 'Balanced', 'desc': 'Equilíbrio entre estabilidade emocional e foco.'},
        }
    },
    'rs1805087': {
        'gene': 'MTR',
        'name': 'A2756G',
        'type': 'Methylation',
        'risk_allele': 'G',
        'interpretations': {
            'AA': {'status': 'Normal', 'risk': 'Low', 'desc': 'Reciclagem normal de homocisteína.'},
            'AG': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Regulação de homocisteína levemente prejudicada.'},
            'GA': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Regulação de homocisteína levemente prejudicada.'},
            'GG': {'status': 'Homozygous Risk', 'risk': 'High', 'desc': 'Maior necessidade de B12 para reciclar homocisteína.'},
        }
    },
    'rs1801394': {
        'gene': 'MTRR',
        'name': 'A66G',
        'type': 'Methylation',
        'risk_allele': 'G',
        'interpretations': {
            'AA': {'status': 'Normal', 'risk': 'Low', 'desc': 'Conversão normal de B12.'},
            'AG': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Conversão de B12 levemente reduzida.'},
            'GA': {'status': 'Heterozygous', 'risk': 'Medium', 'desc': 'Conversão de B12 levemente reduzida.'},
            'GG': {'status': 'Homozygous Risk', 'risk': 'High', 'desc': 'Baixa conversão de B12. Suplementação de B12 (metil/adenosil) recomendada.'},
        }
    },
    # 2. LIPIDS & ALZHEIMER
    'rs429358': {'gene': 'APOE', 'name': 'APOE-1', 'type': 'Lipids'}, # C is E4 marker
    'rs7412':   {'gene': 'APOE', 'name': 'APOE-2', 'type': 'Lipids'}, # T is E2 marker
    'rs708272': { # CETP TaqIB
        'gene': 'CETP',
        'name': 'TaqIB',
        'type': 'Lipids',
        'interpretations': {
            'GG': {'status': 'B1/B1', 'risk': 'High', 'desc': 'Níveis menores de HDL. Risco cardiovascular aumentado.'},
            'AA': {'status': 'B2/B2', 'risk': 'Low', 'desc': 'Níveis maiores de HDL. Proteção cardiovascular.'},
            'AG': {'status': 'B1/B2', 'risk': 'Medium', 'desc': 'Intermediário.'},
            'GA': {'status': 'B1/B2', 'risk': 'Medium', 'desc': 'Intermediário.'},
        }
    },
    # 3. VITAMIN D
    'rs1544410': { # VDR BsmI
        'gene': 'VDR',
        'name': 'BsmI',
        'type': 'Vitamin D',
        'interpretations': {
            'GG': {'status': 'Normal', 'risk': 'Low', 'desc': 'Boa eficiência do recetor (BB).'}, 
            'CC': {'status': 'Normal', 'risk': 'Low', 'desc': 'Boa eficiência do recetor (BB).'}, # CC = GG on reverse strand
            'AA': {'status': 'Risk', 'risk': 'Medium', 'desc': 'Menor eficiência do recetor de Vit D.'},
            'TT': {'status': 'Risk', 'risk': 'Medium', 'desc': 'Menor eficiência do recetor de Vit D.'},
            'AG': {'status': 'Heterozygous', 'risk': 'Low', 'desc': 'Intermediário.'},
            'GA': {'status': 'Heterozygous', 'risk': 'Low', 'desc': 'Intermediário.'},
            'AC': {'status': 'Heterozygous', 'risk': 'Low', 'desc': 'Intermediário.'},
            'CA': {'status': 'Heterozygous', 'risk': 'Low', 'desc': 'Intermediário.'},
        }
    },
    'rs731236': { # VDR TaqI
        'gene': 'VDR',
        'name': 'TaqI',
        'type': 'Vitamin D',
        'interpretations': {
            'GG': {'status': 'Normal', 'risk': 'Low', 'desc': 'Eficiência normal.'},
            'AA': {'status': 'Risk', 'risk': 'Medium', 'desc': 'Menor eficiência na utilização de Vit D.'},
            'AG': {'status': 'Heterozygous', 'risk': 'Low', 'desc': 'Intermediário.'},
        }
    },
    # 4. DETOX
    'rs4880': {
        'gene': 'SOD2',
        'name': 'Val16Ala',
        'type': 'Detox',
        'interpretations': {
            'CC': {'status': 'Ala/Ala', 'risk': 'Low', 'desc': 'Alta eficiência antioxidante mitocondrial.'},
            'GG': {'status': 'Val/Val', 'risk': 'High', 'desc': 'Menor transporte para mitocôndria. Risco de stress oxidativo elevado.'}, # G or T? Usually T=Val.
            'TT': {'status': 'Val/Val', 'risk': 'High', 'desc': 'Menor transporte para mitocôndria. Risco de stress oxidativo elevado.'},
            'CG': {'status': 'Val/Ala', 'risk': 'Medium', 'desc': 'Intermediário.'},
            'CT': {'status': 'Val/Ala', 'risk': 'Medium', 'desc': 'Intermediário.'},
        }
    },
    'rs1695': {
        'gene': 'GSTP1',
        'name': 'Ile105Val',
        'type': 'Detox',
        'interpretations': {
            'AA': {'status': 'Ile/Ile', 'risk': 'Low', 'desc': 'Detoxificação fase II normal.'},
            'GG': {'status': 'Val/Val', 'risk': 'High', 'desc': 'Detoxificação reduzida de xenobióticos/metais pesados.'},
            'AG': {'status': 'Ile/Val', 'risk': 'Medium', 'desc': 'Intermediário.'},
            'GA': {'status': 'Ile/Val', 'risk': 'Medium', 'desc': 'Intermediário.'},
        }
    }
}

import re

def load_dna(filepath):
    """Loads DNA raw data into a dict {rsid: genotype}."""
    dna_data = {}
    rs_pattern = re.compile(r'(rs\d+)')
    
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            if len(row) >= 4:
                raw_id = row[0]
                genotype = row[3]
                
                # Extract clean RSID
                match = rs_pattern.search(raw_id)
                if match:
                    rsid = match.group(1)
                    
                    # Store if new or if upgrading from no-call/bad-call
                    existing = dna_data.get(rsid, '--')
                    is_valid = genotype not in ['--', 'II', 'DD', 'DI'] and len(genotype) == 2
                    is_existing_valid = existing not in ['--', 'II', 'DD', 'DI'] and len(existing) == 2
                    
                    if is_valid and not is_existing_valid:
                        dna_data[rsid] = genotype
                    elif is_valid and is_existing_valid:
                        # Keep existing, or overwrite? Usually first occurrence is fine, but dupseq might be better?
                        # Let's assume the standard rsid (shorter raw_id) is better?
                        if len(raw_id) < 20: # arbitrary check for clean ID
                             dna_data[rsid] = genotype
                    elif rsid not in dna_data:
                        dna_data[rsid] = genotype

    return dna_data

def determine_apoe(dna_data):
    """Determines APOE status based on rs429358 and rs7412."""
    g1 = dna_data.get('rs429358', 'N/A') # 112 (C=E4, T=E3)
    g2 = dna_data.get('rs7412', 'N/A')   # 158 (C=E3/E4, T=E2)
    
    # Normalize invalid calls
    if g1 in ['--', 'II', 'DD', 'DI']: g1 = 'N/A'
    if g2 in ['--', 'II', 'DD', 'DI']: g2 = 'N/A'
    
    status = "Unknown"
    risk = "Unknown"
    desc = "Dados insuficientes."
    
    # Check if both present
    if g1 != 'N/A' and g2 != 'N/A':
        # E4/E4: rs429358 CC, rs7412 CC
        if g1 == 'CC' and g2 == 'CC': status = 'E4/E4'
        # E3/E4: rs429358 CT, rs7412 CC
        elif 'C' in g1 and 'T' in g1 and g2 == 'CC': status = 'E3/E4'
        # E3/E3: rs429358 TT, rs7412 CC
        elif g1 == 'TT' and g2 == 'CC': status = 'E3/E3'
        # E2/E3: rs429358 TT, rs7412 CT
        elif g1 == 'TT' and 'C' in g2 and 'T' in g2: status = 'E2/E3'
        # E2/E2: rs429358 TT, rs7412 TT
        elif g1 == 'TT' and g2 == 'TT': status = 'E2/E2'
        # E2/E4: rs429358 CT, rs7412 CT (Rare)
        elif 'C' in g1 and 'T' in g1 and 'C' in g2 and 'T' in g2: status = 'E2/E4'
    
    # Handle partial
    elif g2 == 'CC': # No E2 allele. Must be E3 or E4.
        status = "E3/E3 (Likely) or E3/E4 / E4/E4"
        risk = "Variable"
        desc = "Marcador E2 ausente (rs7412=CC). Marcador E4 (rs429358) não disponível. Assume-se risco padrão (E3/E3), mas E4 não pode ser excluído."
    elif g2 == 'TT': # Homozygous E2 allele?
        status = "E2/E2 (Likely)"
        risk = "Low"
        desc = "Marcador E2 em dose dupla (rs7412=TT). Provável proteção contra Alzheimer."
    elif 'T' in g2 and 'C' in g2: # E2 carrier
        status = "E2/E3 or E2/E4"
        risk = "Low/Neutral"
        desc = "Portador de alelo E2. Geralmente protetor ou neutro."
    
    # Final Risk Assessment if fully determined
    if 'E4' in status and 'Likely' not in status:
        if status == 'E4/E4':
            risk = "Very High"
            desc = "Alto risco de Alzheimer. Resposta inflamatória alta a gorduras saturadas. Dieta Carnívora requer monitorização lipídica rigorosa."
        elif 'E3/E4' in status:
            risk = "High"
            desc = "Risco aumentado de Alzheimer (Heterozigoto E4). Cuidado com gorduras saturadas em excesso."
        elif 'E2/E4' in status:
            risk = "Medium"
            desc = "E2 protege parcialmente contra o risco do E4."
    elif status == 'E3/E3':
        risk = "Neutral"
        desc = "Risco médio (padrão populacional). Metabolismo de gorduras normal."
    elif 'E2' in status and 'Likely' not in status:
        risk = "Low"
        desc = "Proteção contra Alzheimer, mas risco de hiperlipidemía tipo III (triglicéridos)."
        
    return {'genotype': f"{g1} + {g2}", 'status': status, 'risk': risk, 'desc': desc}

def analyze_snp(rsid, genotype, definition):
    if genotype == 'N/A':
        return {'genotype': 'N/A', 'status': 'N/A', 'risk': 'Unknown', 'desc': 'SNP não encontrado no ficheiro.'}
    
    # Check specific interpretations first
    interps = definition.get('interpretations', {})
    
    # Try exact match
    if genotype in interps:
        return interps[genotype]
    
    # Try reverse match (e.g. AG vs GA)
    rev_genotype = genotype[::-1]
    if rev_genotype in interps:
        return interps[rev_genotype]
        
    # Default fallback
    return {'genotype': genotype, 'status': 'Unknown', 'risk': 'Unknown', 'desc': f'Interpretação não definida para {genotype}.'}

def main():
    print(f"Loading {INPUT_FILE}...")
    try:
        dna_data = load_dna(INPUT_FILE)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    analysis_results = []
    
    # Process regular SNPs
    for rsid, definition in SNP_DB.items():
        if rsid in ['rs429358', 'rs7412']: continue # Handle APOE separately
        
        genotype = dna_data.get(rsid, 'N/A')
        result = analyze_snp(rsid, genotype, definition)
        
        entry = {
            'rsid': rsid,
            'gene': definition['gene'],
            'genotype': genotype,
            'status': result.get('status', 'Unknown'),
            'risk': result.get('risk', 'Unknown'),
            'description': result.get('desc', ''),
            'category': definition['type']
        }
        analysis_results.append(entry)

    # Process APOE
    apoe_res = determine_apoe(dna_data)
    analysis_results.append({
        'rsid': 'rs429358/rs7412',
        'gene': 'APOE',
        'genotype': apoe_res['genotype'],
        'status': apoe_res['status'],
        'risk': apoe_res['risk'],
        'description': apoe_res['desc'],
        'category': 'Lipids'
    })

    # Save JSON
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(analysis_results, f, indent=2)
    print(f"Saved {OUTPUT_JSON}")

    # Generate MD Summary
    generate_md_summary(analysis_results)

def generate_md_summary(results):
    lines = ["# Resumo Executivo: Análise de DNA (Longevidade & Carnívora)\n"]
    
    # Group by category
    categories = {}
    for r in results:
        cat = r['category']
        if cat not in categories: categories[cat] = []
        categories[cat].append(r)
        
    # Highlights (High Risk)
    lines.append("## 🚨 Pontos de Atenção (Riscos Identificados)\n")
    high_risks = [r for r in results if 'High' in r['risk'] or 'Warrior' in r['status']] # Including Warrior as a "feature" to note
    if not high_risks:
        lines.append("Nenhum risco genético *elevado* detetado nos marcadores analisados.\n")
    else:
        for r in high_risks:
            lines.append(f"- **{r['gene']} ({r['status']})**: {r['description']}")
            
    lines.append("\n## ✅ Pontos Fortes\n")
    strengths = [r for r in results if r['risk'] == 'Low' or ('Normal' in r['status'] and r['risk'] != 'High')]
    if not strengths:
        lines.append("Nenhum ponto forte específico destacado.\n")
    else:
        for r in strengths:
            lines.append(f"- **{r['gene']}**: Genótipo favorável/normal. {r['description']}")

    lines.append("\n## 🧬 Análise Detalhada por Categoria\n")
    
    order = ['Methylation', 'Lipids', 'Vitamin D', 'Detox']
    for cat in order:
        if cat in categories:
            lines.append(f"### {cat}")
            for r in categories[cat]:
                icon = "⚠️" if "High" in r['risk'] else "ℹ️"
                if r['risk'] == 'Low': icon = "✅"
                
                lines.append(f"- {icon} **{r['gene']} ({r['rsid']})**: `{r['genotype']}` -> {r['description']}")
            lines.append("")

    lines.append("## 💡 Recomendações Personalizadas\n")
    
    recs = []
    # Methylation Recs
    mthfr = [r for r in results if r['gene'] == 'MTHFR' and ('High' in r['risk'] or 'Medium' in r['risk'])]
    if mthfr:
        recs.append("- **Metilação**: Considere suplementar com **Metilfolato (5-MTHF)** e **Metilcobalamina** em vez de ácido fólico sintético. Consuma fígado (rico em folato natural).")
    
    comt = [r for r in results if r['gene'] == 'COMT']
    if comt:
        c = comt[0]
        if 'Warrior' in c['status'] and 'Worrier' not in c['status']:
            recs.append("- **COMT Rápido**: O seu sistema elimina catecolaminas rapidamente. Pode beneficiar de **magnésio**, **chá verde** (inibe levemente COMT) e evitar excesso de estimulantes.")
        elif 'Worrier' in c['status']:
            recs.append("- **COMT Lento**: Evite excesso de catecolaminas (stress, cafeína em excesso). Magnésio é crucial. Atenção à acumulação de estrogénios.")

    # Lipids Recs
    apoe = [r for r in results if r['gene'] == 'APOE'][0]
    if 'E4' in apoe['status']:
        recs.append("- **APOE4**: Sensibilidade a gorduras saturadas. Na dieta carnívora, priorize cortes mais magros, peixe (Omega-3) e considere azeite se flexível. Monitorize LDL e ApoB frequentemente.")
    
    # Vit D Recs
    vdr = [r for r in results if r['gene'] == 'VDR' and ('High' in r['risk'] or 'Medium' in r['risk'])]
    if vdr:
        recs.append("- **Vitamina D**: Os seus recetores são menos eficientes. Mantenha níveis séricos de Vit D3 no limite superior (60-80 ng/mL). Exposição solar e suplementação com K2 são vitais.")
        
    # Detox Recs
    sod_list = [r for r in results if r['gene'] == 'SOD2']
    if sod_list:
        s = sod_list[0]
        if 'Val/Val' in s.get('status', ''):
             recs.append("- **Antioxidantes**: Menor proteção mitocondrial natural (SOD2 Val/Val). Evite treinos exaustivos sem recuperação adequada. Sono de qualidade é prioridade.")

    if not recs:
        recs.append("- Mantenha um estilo de vida saudável e repita exames de sangue anuais.")
        
    for rec in recs:
        lines.append(rec)

    with open(OUTPUT_MD, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Saved {OUTPUT_MD}")

if __name__ == "__main__":
    main()
