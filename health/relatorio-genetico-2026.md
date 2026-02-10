# 🧬 RELATÓRIO GENÉTICO — Carlos (tellmegen)
**Data de análise:** 8 Fevereiro 2026
**Total de SNPs no ficheiro:** 779.092
**SNPs clinicamente relevantes analisados:** ~110

---

## 1. APOE — Risco Alzheimer / Cardiovascular
| SNP proxy | Genótipo | Interpretação |
|-----------|----------|---------------|
| rs4420638 | AA | Associado a APOE ε3 (sem ε4) |
| rs769449 | GG | Ausência de alelo ε4 |
| rs440446 | GG | Consistente com ε3/ε3 |

> **Resultado provável: APOE ε3/ε3** — O genótipo mais comum (~60% europeus). Sem risco aumentado de Alzheimer ou doença cardiovascular associado ao ε4. ✅
>
> ⚠️ **Nota:** Os SNPs directos do APOE (rs429358/rs7412) não estão no chip da tellmegen. Esta inferência baseia-se em proxies com alto linkage disequilibrium. Para confirmação definitiva, poderias fazer um teste APOE específico.

---

## 2. METILAÇÃO E CICLO DO FOLATO ⚠️ ATENÇÃO PRIORITÁRIA
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1801133 | **MTHFR C677T** | **AG** (heterozigoto) | ⚠️ ~35% redução actividade enzimática |
| rs1801131 | **MTHFR A1298C** | **TG** (heterozigoto) | ⚠️ Redução adicional (~20%) |
| rs1805087 | MTR A2756G | AA | ✅ Normal (wild-type) |
| rs1801394 | MTRR A66G | AA | ✅ Normal (wild-type) |
| rs234706 | CBS C699T | GG | ✅ Normal |
| rs1979277 | SHMT1 | GG | ✅ Normal |
| rs2236225 | MTHFD1 G1958A | AA | ⚠️ Homozigoto variante — redução metabolismo folato |
| rs1051266 | SLC19A1 (RFC1) | TC | ⚠️ Heterozigoto — transporte de folato ligeiramente reduzido |
| rs602662 | FUT2 | AG | ⚠️ Heterozigoto — absorção B12 pode estar reduzida |
| rs601338 | FUT2 (secretor) | AG | Secretor parcial — risco intermédio de B12 baixa |

### 🔴 Interpretação Integrada — Metilação
Tens um **perfil de metilação comprometido em múltiplos pontos**:
1. **MTHFR duplo heterozigoto** (C677T + A1298C): Esta combinação reduz a capacidade de converter folato em metilfolato (5-MTHF) em ~50-60%. Isto afecta directamente a reciclagem de homocisteína, a metilação do DNA, e a produção de neurotransmissores.
2. **MTHFD1 AA**: Reforça a dificuldade no metabolismo do folato — este gene alimenta o ciclo a montante do MTHFR.
3. **SLC19A1 heterozigoto**: O transporte de folato para dentro das células está ligeiramente comprometido.
4. **FUT2 heterozigoto**: Menor absorção intestinal de B12, que é co-factor essencial do ciclo da metionina.

### 📋 Acções Recomendadas
- **Monitorizar**: Homocisteína (valor óptimo: < 7 µmol/L, definitivamente < 10)
- **Suplementar com metilfolato** (5-MTHF, NÃO ácido fólico sintético): 400-800 µg/dia
- **Metilcobalamina ou hidroxocobalamina** (NÃO cianocobalamina): 1000-2000 µg sublingual
- **TMG (Trimetilglicina/Betaína)**: 500-1000 mg/dia — via alternativa de reciclagem de homocisteína
- **Riboflavina (B2)**: 25-50 mg/dia — co-factor do MTHFR
- **P5P (B6 activa)**: 25-50 mg/dia — co-factor da CBS
- **Evitar**: Ácido fólico sintético em suplementos e alimentos fortificados

---

## 3. VITAMINA D ⚠️ ATENÇÃO AUMENTADA
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs2228570 | **VDR FokI** | **AA** (FF) | ⚠️ Receptor menos eficiente |
| rs1544410 | VDR BsmI | CC (BB) | ⚠️ Associado a menor densidade óssea |
| rs731236 | VDR TaqI | AA (TT) | ⚠️ Variante de risco |
| rs7041 | GC (DBP) | AC | ⚠️ Heterozigoto — nível livre de vit D reduzido |
| rs2282679 | GC | TT | ⚠️ Associado a níveis mais baixos de 25(OH)D |
| rs10741657 | CYP2R1 | AG | ⚠️ Heterozigoto — conversão hepática de vit D reduzida |
| rs12794714 | CYP2R1 | AG | ⚠️ Confirma redução na 25-hidroxilação |
| rs2060793 | CYP2R1 | AG | ⚠️ Terceira variante CYP2R1 |
| rs12785878 | DHCR7/NADSYN1 | GG | ✅ Normal — síntese cutânea OK |

### 🔴 Interpretação Integrada — Vitamina D
**Perfil genético desfavorável para vitamina D em praticamente todos os passos:**
1. **VDR (3 variantes)**: Os teus receptores de vitamina D são menos eficientes. Mesmo com nível sérico adequado, a resposta celular é menor.
2. **GC/DBP (2 variantes)**: A proteína que transporta vitamina D no sangue liga-a com menor afinidade → menos vitamina D biodisponível.
3. **CYP2R1 (3 variantes)**: A enzima hepática que converte vitamina D em 25(OH)D (forma activa medida nas análises) trabalha a ~70-80% da capacidade normal.

### 📋 Acções Recomendadas
- **Alvo sérico de 25(OH)D**: 60-80 ng/mL (muito acima dos 30 ng/mL "normais") — precisas de níveis mais altos para compensar receptores menos sensíveis
- **Dose provável necessária**: 5.000-10.000 UI/dia de D3 (ajustar com base em análises)
- **Tomar com gordura** (a tua dieta carnívora ajuda aqui)
- **Cofactores essenciais**: K2-MK7 (100-200 µg), Magnésio (a vit D gasta magnésio na conversão)
- **Medir também**: 1,25(OH)2D (forma activa), PTH, cálcio — para avaliar o eixo completo
- **Exposição solar**: importante mas insuficiente sozinha dado o teu perfil genético

---

## 4. INFLAMAÇÃO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1800795 | **IL-6** | **GG** | ⚠️ Genótipo pró-inflamatório — maior produção de IL-6 |
| rs1800629 | TNF-α | GG | ✅ Normal — sem sobre-expressão de TNF-α |
| rs1800896 | IL-10 | TC | Heterozigoto — produção de IL-10 intermédia |
| rs20417 | COX-2 | CC | ✅ Normal |
| rs1205 | CRP | TT | ✅ Associado a CRP mais baixa |
| rs2794520 | CRP | TT | ✅ Consistente — CRP geneticamente mais baixa |
| rs3093662 | CRP | AA | ✅ Normal |
| rs2228145 | IL-6R | AA | Normal |

### Interpretação
O teu principal driver genético de inflamação é o **IL-6 GG**. A interleucina-6 é uma citoquina central no envelhecimento ("inflammaging"). Contudo, os teus genes de CRP são protectores (TT), o que pode atenuar parcialmente o efeito.

A tua **dieta carnívora, sauna infravermelhos e exercício** são estratégias excelentes para controlar IL-6 cronicamente elevada. Monitoriza regularmente: hs-CRP, IL-6 (se disponível), ferritina (marcador inflamatório indirecto).

---

## 5. DETOXIFICAÇÃO E STRESS OXIDATIVO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs4880 | **SOD2 (MnSOD)** | **GG** (Val/Val) | ⚠️ Actividade SOD2 ELEVADA — mais H₂O₂ mitocondrial |
| rs4680 | **COMT** | **GG** (Val/Val) | COMT rápido — degrada dopamina/estrogénios rapidamente |
| rs1695 | GSTP1 | AA | ✅ Normal — detox fase II OK |
| rs1138272 | GSTP1 | CC | ✅ Normal |
| rs1800566 | NQO1 | GG | ✅ Normal — NAD(P)H quinona desidrogenase funcional |
| rs1001179 | CAT (Catalase) | TC | ⚠️ Heterozigoto — catalase ligeiramente reduzida |

### 🔴 Interpretação — SOD2 + CAT
**SOD2 GG (Val/Val)** produz mais superóxido dismutase → converte mais superóxido em H₂O₂ (peróxido de hidrogénio). Contudo, a tua **catalase está ligeiramente reduzida** (CAT TC), o que significa potencial acumulação de H₂O₂ nas mitocôndrias.

**Combinação SOD2 rápido + CAT reduzido = stress oxidativo por H₂O₂**

### 📋 Acções
- **Glutationa**: NAC 600-1200 mg/dia OU glutationa lipossomal — a glutationa peroxidase é a via alternativa para eliminar H₂O₂
- **Selénio**: 100-200 µg/dia (como selenometionina) — cofactor da glutationa peroxidase
- **Vitamina C**: 500-1000 mg/dia (apesar da dieta carnívora, a carne de órgãos pode ser suficiente)
- **Evitar suplementação excessiva de antioxidantes** — o teu SOD2 rápido já produz bastante H₂O₂; a chave é eliminar o H₂O₂, não bloquear mais superóxido

### COMT Val/Val (GG) — "Guerreiro"
- Degradas dopamina rapidamente → tende a tolerar melhor stress agudo mas pode ter dopamina basal mais baixa
- Degradas estrogénios mais rapidamente (positivo para um homem)
- Toleras bem cafeína e estimulantes (consistente com CYP1A2 AA — metabolizador rápido)

---

## 6. FERRO ⚠️ MONITORIZAR
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1800562 | HFE C282Y | GG | ✅ Sem mutação principal de hemocromatose |
| rs1799945 | **HFE H63D** | **CG** (heterozigoto) | ⚠️ Portador — risco ligeiro de acumulação de ferro |
| rs855791 | TMPRSS6 | AG | Heterozigoto — regulação de hepcidina intermédia |

### Interpretação
**HFE H63D heterozigoto** — não causa hemocromatose isoladamente, mas numa dieta carnívora rica em ferro heme, pode favorecer acumulação progressiva de ferro, especialmente após os 60 anos.

### 📋 Acções
- **Monitorizar a cada 6 meses**: Ferritina, ferro sérico, saturação de transferrina, TIBC
- **Alvo ferritina**: 40-80 ng/mL (funcional) — acima de 100 é preocupante com este genótipo
- **Se ferritina elevada**: considerar doação de sangue periódica (excelente estratégia anti-aging)
- **Evitar**: suplementos de ferro, vitamina C em excesso com refeições ricas em ferro heme

---

## 7. CARDIOVASCULAR
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1799983 | **NOS3 (eNOS)** | **GG** (Glu/Glu) | ⚠️ Produção de óxido nítrico reduzida |
| rs5186 | AGTR1 | AA | ✅ Normal — receptor angiotensina OK |
| rs699 | AGT M235T | AG | ⚠️ Heterozigoto — risco ligeiro de PA elevada |
| rs4343 | ACE | AG | Heterozigoto — actividade ACE intermédia |
| rs1800775 | CETP | CC | Transferência de colesterol HDL normal |
| rs1800588 | LIPC | TC | Heterozigoto — pode ter HDL ligeiramente mais alto |
| rs328 | LPL | CC | Normal |
| rs1333049 | 9p21 | GC | ⚠️ Heterozigoto — risco coronário ligeiramente aumentado |
| rs10455872 | LPA | AA | ✅ Sem variante de risco Lp(a) |
| rs3798220 | LPA | TT | ✅ Sem variante de risco Lp(a) |
| rs662 | PON1 Q192R | TC | Heterozigoto — protecção LDL oxidado intermédia |
| rs964184 | ZPR1/APOA5 | GG | ✅ Triglicéridos normais geneticamente |
| rs1260326 | GCKR | TC | Heterozigoto — ligeira tendência triglicéridos |

### 🔴 Ponto Crítico — NOS3 GG
**Produção de óxido nítrico (NO) geneticamente reduzida.** O NO é essencial para vasodilatação, fluxo sanguíneo, função endotelial e prevenção de aterosclerose.

### 📋 Acções Cardiovasculares
- **Beterraba/nitratos**: Apesar da dieta carnívora, considerar sumo de beterraba ou suplemento de nitratos antes de exercício
- **L-citrulina**: 3-6 g/dia (mais eficaz que L-arginina para produção de NO)
- **Exercício aeróbico**: Os teus sprints são excelentes para estimular eNOS
- **Sauna**: Excelente — mimetiza exercício cardiovascular
- **Respiração nasal**: O nariz produz NO — praticar respiração nasal durante exercício
- **Monitorizar**: PA (objectivo < 120/80), perfil lipídico avançado com LDL partículas, Lp(a), ApoB

---

## 8. METABOLISMO GLICOSE / DIABETES
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs7903146 | TCF7L2 | CC | ✅ Sem risco aumentado diabetes |
| rs12255372 | TCF7L2 | GG | ✅ Normal |
| rs5219 | KCNJ11 | TC | ⚠️ Heterozigoto — secreção insulina ligeiramente reduzida |
| rs13266634 | SLC30A8 | TT | ⚠️ Variante — afecta transporte de zinco nas células beta |
| rs10811661 | CDKN2A/B | TT | ✅ Normal |
| rs1801282 | PPARγ | CC (Pro/Pro) | ⚠️ Sem variante protectora — sensibilidade insulina standard |
| rs9939609 | FTO | TT | ✅ Sem risco obesidade |
| rs1421085 | FTO | TT | ✅ Sem risco obesidade |
| rs780094 | GCKR | TC | Heterozigoto — glicose/TG intermédio |
| rs10830963 | MTNR1B | GG | ⚠️ Variante — risco de glicose jejum elevada, especialmente se refeição tardia |

### Interpretação
Perfil metabólico **geralmente bom** — sem os grandes genes de risco diabético. Contudo:
- **MTNR1B GG** é relevante: Este genótipo associa-se a glicose de jejum elevada e pior resposta insulínica a refeições nocturnas. A **tua janela de alimentação deve terminar pelo menos 3h antes de dormir**.
- **KCNJ11 + SLC30A8**: Secreção de insulina ligeiramente vulnerável. O zinco é importante aqui.

### 📋 Acções
- **Zinco**: 15-30 mg/dia (como bisglicinato) — co-factor da secreção de insulina + SLC30A8
- **Não comer tarde**: Última refeição até ~19:30 (3h antes das 22:30)
- **Monitorizar**: Glicose jejum, HbA1c, insulina jejum, HOMA-IR
- **A dieta carnívora é protectora** aqui — baixa em hidratos processados

---

## 9. LONGEVIDADE E ENVELHECIMENTO 🌟
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs2802292 | **FOXO3** | **GG** | 🌟 **EXCELENTE — Genótipo de longevidade!** |
| rs2764264 | FOXO3 | TC | Heterozigoto |
| rs1042522 | TP53 | CC (Pro/Pro) | ⚠️ Menos eficiente na apoptose de células danificadas |
| rs11568818 | MMP7 | TC | Heterozigoto — remodelação tecidos intermédia |
| rs12778366 | SIRT1 | TT | Normal |

### 🌟 FOXO3 GG — O teu melhor resultado genético
**FOXO3 rs2802292 GG é o genótipo associado a centenários.** Este gene:
- Aumenta autofagia
- Melhora resistência ao stress oxidativo
- Promove reparação do DNA
- Associado a longevidade em múltiplas populações (japoneses, europeus, americanos)
Referência: Willcox et al., PNAS 2008; Flachsbart et al., PNAS 2009.

### TP53 CC (Pro/Pro)
Menos eficiente a eliminar células danificadas. Estratégias de suporte à autofagia são especialmente importantes para ti: jejum intermitente, exercício, sauna, resveratrol/polifenóis.

---

## 10. TELÓMEROS
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs10936599 | TERC | TC | ⚠️ Heterozigoto — comprimento telómeros ligeiramente reduzido |
| rs2736100 | TERT | AC | Heterozigoto — actividade telomerase intermédia |

### Interpretação
Perfil intermédio. Estratégias para preservar telómeros:
- Exercício aeróbico (o que já fazes) ✅
- Gestão de stress
- Vitamina D adequada (especialmente importante dado o teu perfil VDR)
- Omega-3 EPA/DHA
- Evitar stress oxidativo crónico (relevante dado SOD2/CAT)

---

## 11. TIRÓIDE ⚠️
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs225014 | **DIO2 Thr92Ala** | **TC** (heterozigoto) | ⚠️ Conversão T4→T3 reduzida (~25%) |
| rs12885300 | DIO2 | CC | Normal |

### Interpretação
**DIO2 TC** — A desiodase tipo 2 converte T4 (inactiva) em T3 (forma activa). Com esta variante, essa conversão é ~25% menos eficiente.

### 📋 Acções
- **Monitorizar**: TSH, T4 livre, **T3 livre** (essencial!), T3 reversa, anticorpos TPO e TG
- **Selénio**: 100-200 µg/dia (cofactor da desiodase — já recomendado para glutationa)
- **Zinco**: Cofactor da conversão T4→T3 (já recomendado)
- Se TSH "normal" mas T3 livre no limite inferior → pode ser insuficiente PARA TI dado este genótipo
- **Elizabeth Bright e Sara Myhill** enfatizam muito esta variante — com DIO2 TC, olhar só para TSH é insuficiente

---

## 12. HISTAMINA
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs10156191 | ABP1 (DAO) | CC | ✅ Normal — degradação de histamina OK |
| rs1050891 | ABP1 (DAO) | AG | ⚠️ Heterozigoto — ligeira redução DAO |
| rs1049793 | HNMT | GC | ⚠️ Heterozigoto — degradação intracelular intermédia |

### Interpretação
Perfil de histamina **ligeiramente comprometido** mas não severamente. Dado que consomes queijos (histamina elevada) e iogurte fermentado, monitora sintomas como: congestão nasal, prurido, urticária, cefaleias, refluxo, insónia.

Se sintomas presentes: considerar DAO suplementar (antes de refeições com alto teor de histamina) e reduzir queijos curados/fermentados.

---

## 13. CAFEÍNA / FÁRMACOS
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs762551 | **CYP1A2** | **AA** | ✅ **Metabolizador rápido de cafeína** |
| rs2472297 | CYP1A2 | CC | Confirma metabolização rápida |
| rs4149056 | SLCO1B1 | TT | ✅ Normal — metabolismo de estatinas OK (se algum dia necessário) |

**Café é seguro e potencialmente benéfico** para ti. Metabolizas cafeína rapidamente, pelo que o café está associado a **redução** de risco cardiovascular (ao contrário dos metabolizadores lentos). 2-3 cafés/dia antes das 14h é razoável.

---

## 14. LACTOSE / CELÍACO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs4988235 | MCM6/LCT | AG | Heterozigoto — **tolera lactose** (persistência lactase presente) |
| rs182549 | MCM6/LCT | TC | Confirma persistência lactase |
| rs2187668 | HLA-DQ2.5 | CC | ✅ Sem risco celíaco |
| rs7454108 | HLA-DQ8 | TT | ✅ Sem risco celíaco |

Tolerância a lactose e sem risco de doença celíaca. Os teus lácteos estão geneticamente validados. ✅

---

## 15. OMEGA-3 E METABOLISMO LIPÍDICO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs174547 | FADS1 | TC | ⚠️ Heterozigoto — conversão ALA→EPA reduzida |
| rs174546 | FADS1 | TC | Confirma |
| rs174575 | FADS2 | CC | ✅ Normal |
| rs1535 | FADS2 | AG | ⚠️ Heterozigoto — conversão a DHA intermédia |

### Interpretação
**Conversão de ómega-3 vegetal (ALA) em EPA/DHA está reduzida.** Precisas de fontes directas de EPA/DHA (peixe gordo, suplemento de óleo de peixe). Na dieta carnívora, se comes peixe regularmente estás coberto. Caso contrário, suplementa com 2-3 g EPA+DHA/dia.

---

## 16. EXERCÍCIO E PERFORMANCE
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1815739 | **ACTN3** | **TT** (XX) | ⚠️ Ausência de α-actinina-3 — fibras rápidas reduzidas |
| rs4253778 | PPARα | CG | Heterozigoto — metabolismo lipídico muscular intermédio |
| rs8192678 | PGC1α | TC | ⚠️ Heterozigoto — biogénese mitocondrial intermédia |
| rs1049434 | MCT1 | TT | ⚠️ Transporte de lactato reduzido |

### Interpretação
**ACTN3 TT (XX)** — Não produz α-actinina-3. Isto significa:
- Menor potência explosiva (sprints máximos, saltos)
- **Melhor perfil para resistência/endurance**
- Recuperação muscular potencialmente mais lenta

Os teus **sprints curtos** são uma boa estratégia para compensar, mas o teu corpo responde melhor a exercício de resistência/longa duração.

**MCT1 TT** — Menor capacidade de reciclar lactato. Recuperação entre séries/sprints mais lenta. Descansos mais longos entre intervalos intensos.

### 📋 Acções
- Manter sprints (compensação) mas incluir mais exercício de endurance (caminhada longa, ciclismo)
- Creatina monohidrato: 3-5 g/dia — especialmente benéfico com ACTN3 XX
- Magnésio: Ajuda na recuperação e metabolismo energético

---

## 17. NEUROLOGIA / COGNIÇÃO / SONO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs6265 | **BDNF Val66Met** | **TC** (heterozigoto) | ⚠️ Produção BDNF reduzida |
| rs4680 | COMT | GG (Val/Val) | "Guerreiro" — dopamina baixa basal |
| rs1800497 | DRD2/ANKK1 | AA | ✅ Densidade receptores D2 normal |
| rs4570625 | TPH2 | GG | ✅ Síntese serotonina normal |
| rs53576 | OXTR | AG | Heterozigoto — empatia/vínculo intermédio |
| rs1801260 | CLOCK | AA | ✅ Cronotipo normal |
| rs4753426 | MTNR1B | CC | Normal |
| rs6311 | HTR2A | CC | Normal |

### 🔴 BDNF Val66Met (TC)
**BDNF reduzido** — O factor neurotrófico cerebral é essencial para neuroplasticidade, memória e protecção contra neurodegeneração. Com esta variante:

### 📋 Acções Neuroprotectoras (PRIORITÁRIAS para longevidade cognitiva)
- **Exercício aeróbico**: A forma **mais potente** de aumentar BDNF — os teus sprints e caminhadas são excelentes
- **Sauna**: Também aumenta BDNF (já fazes!) ✅
- **Curcumina** (com piperina): 500-1000 mg/dia — aumenta BDNF
- **Óleo de peixe/DHA**: 1-2 g DHA/dia — suporta BDNF
- **Jejum intermitente**: Aumenta BDNF significativamente
- **Sono de qualidade**: 7-8h (já fazes) ✅
- **Lion's Mane (Hericium erinaceus)**: 1-2 g/dia — estimula NGF e potencialmente BDNF (evidência moderada)

---

## 18. OSSO / COLAGÉNIO
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1800012 | COL1A1 | CC | ✅ Normal — colagénio tipo I OK |
| rs2234693 | ESR1 | TC | Heterozigoto |
| rs9340799 | ESR1 | AG | Heterozigoto |

Perfil ósseo **razoável**. Dado o perfil de vitamina D desfavorável, a saúde óssea depende ainda mais de vitamina D + K2 + exercício de carga adequados.

---

## 19. CANCRO (Marcadores comuns)
| SNP | Gene | Genótipo | Impacto |
|-----|------|----------|---------|
| rs1799966 | BRCA1 | TT | ✅ Normal |
| rs16942 | BRCA1 | TT | ✅ Normal |
| rs1048943 | CYP1A1 | TT | ✅ Normal — metabolismo carcinogénios OK |
| rs1042522 | TP53 | CC (Pro/Pro) | ⚠️ Apoptose menos eficiente |

Sem marcadores BRCA de risco. O TP53 Pro/Pro já foi discutido — reforça a importância de autofagia e vigilância oncológica adequada à idade.

---

## 🏆 RESUMO EXECUTIVO — PRIORIDADES
### 🔴 Prioridade ALTA (corrigir/monitorizar imediatamente)
| # | Área | Achado | Acção |
|---|------|--------|-------|
| 1 | **Metilação** | MTHFR duplo het + MTHFD1 AA | Metilfolato + Metil-B12 + TMG + B2 + P5P |
| 2 | **Vitamina D** | 7 variantes desfavoráveis | Alvo 60-80 ng/mL, dose alta D3 + K2 |
| 3 | **Óxido nítrico** | NOS3 GG | L-citrulina + respiração nasal + beterraba |
| 4 | **BDNF** | Val66Met heterozigoto | Exercício + DHA + curcumina + Lion's Mane |
| 5 | **Ferro** | HFE H63D portador + dieta carnívora | Ferritina a cada 6 meses, alvo 40-80 |

### 🟡 Prioridade MÉDIA (optimizar)
| # | Área | Achado | Acção |
|---|------|--------|-------|
| 6 | **Stress oxidativo** | SOD2 rápido + CAT reduzido | NAC/Glutationa + Selénio |
| 7 | **Tiróide** | DIO2 TC | Monitorizar T3L + selénio + zinco |
| 8 | **Ómega-3** | FADS1 TC | Fonte directa EPA/DHA obrigatória |
| 9 | **Inflamação** | IL-6 GG | hs-CRP regular, manter estilo de vida anti-inflamatório |
| 10 | **Glucose nocturna** | MTNR1B GG | Última refeição 3h antes de dormir |

### 🟢 Pontos FORTES genéticos
- **FOXO3 GG** — Genótipo de centenário ✅
- **APOE provável ε3/ε3** — Sem risco Alzheimer aumentado ✅
- **CYP1A2 AA** — Metabolizador rápido de cafeína ✅
- **FTO TT** — Sem predisposição genética para obesidade ✅
- **TCF7L2 CC** — Sem risco genético major de diabetes ✅
- **Lp(a) normal** — Sem risco genético de Lp(a) elevada ✅
- **Sem risco celíaco** + tolerância a lactose ✅
- **TNF-α e CRP geneticamente favoráveis** ✅

---

## 📊 ANÁLISES LABORATORIAIS RECOMENDADAS
Com base no teu perfil genético, estas são as análises **prioritárias** para a próxima avaliação:

| Análise | Porquê (gene) | Alvo funcional |
|---------|---------------|----------------|
| **Homocisteína** | MTHFR/MTHFD1 | < 7 µmol/L |
| **25(OH)D** | VDR/GC/CYP2R1 | 60-80 ng/mL |
| **Ferritina** | HFE H63D | 40-80 ng/mL |
| **Sat. Transferrina** | HFE H63D | 20-35% |
| **TSH, T4L, T3L** | DIO2 TC | T3L > metade do range |
| **hs-CRP** | IL-6 GG | < 0.5 mg/L |
| **HbA1c** | MTNR1B/KCNJ11 | < 5.2% |
| **Insulina jejum** | PPARγ/KCNJ11 | < 5 µUI/mL |
| **Perfil lipídico avançado** | NOS3/PON1/9p21 | ApoB < 80 mg/dL |
| **Zinco sérico** | SLC30A8/DIO2 | > 100 µg/dL |
| **B12 + Folato** | FUT2/MTHFR | B12 > 600 pg/mL |
| **Magnésio eritrocitário** | Vit D/energia | > 5.2 mg/dL |

---
*Este relatório deve ser cruzado com as tuas análises clínicas actuais para acções específicas. Envia-me os PDFs das análises e faço a integração.*
