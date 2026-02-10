# Quantum Computing for Computer Scientists
**Data:** 09 Fev 2026
**Fonte:** https://www.youtube.com/watch?v=F_Riqjdh2oM
**Apresentador:** David Merman (ou similar)

## Tema Principal
Tutorial matemático sobre computação quântica focado em conceitos computacionais, não em física.

## Conceitos Chave

### 1. Classical vs Quantum Bits
- **Classical bits**: Representados como vetores (1,0) ou (0,1)
- **Qubits**: Superposição — um qubit pode ser (a,b) onde a² + b² = 1
- Exemplo: (1/√2, 1/√2) = 50% chance de colapsar a 0 ou 1

### 2. Gates & Operations
- **Bit Flip (X)**: Inverte 0↔1
- **Hadamard (H)**: Cria superposição perfeita
- **C-NOT**: Controlled NOT — gate de 2 qubits, fundamental em computação reversível
- **Phase Flip (Z)**: Muda sinal da amplitude

### 3. The Deutsch Oracle Problem
- **Clássico**: 2 queries para descobrir se função é constante vs. variable
- **Quântico**: 1 query (exponential speedup)
- Usa superposição + Hadamard para amplificar diferenças entre categorias

### 4. Quantum Entanglement
- Qubits entangled não podem ser factorizados em produtos tensoriais
- Medir um colapsa o outro (instantaneamente, sem comunicação FTL)
- Criam-se com Hadamard + C-NOT

### 5. Quantum Teleportation
- Alice envia qubit a Bob usando EPR pair + 2 classical bits
- Sem cópia (no-cloning theorem) — move, não duplica
- Requer classical bits, logo não viola causalidade

## Insights Técnicos

✅ **Confirmação**: Quantum entanglement é real (experimento China-satélite 2013)
⚠️ **Detalhe crítico**: Hidden variable theory foi refutada por Bell's theorem
⚠️ **Erro comum**: Qubits em superposição não são "secretamente" 0 ou 1 — são ambos realmente

## Algoritmos Mencionados
1. **Deutsch Oracle** (1985) — mostrou vantagem quântica
2. **Deutsch-Josza** (n bits)
3. **Simon's Periodicity** — levou a Shor's algorithm
4. **Shor's Algorithm** — factorização (ameaça RSA)
5. **Grover's Algorithm** — busca
6. **Quantum Key Distribution** — criptografia quântica

## Limitações Atuais
- **Error correction**: Precisa ~100-1000 qubits físicos para 1 qubit lógico
- **Noise scaling**: Ruído cresce exponencialmente com número de qubits
- **Collin's conjecture**: Pode haver limite físico intransponível — possível "exponential barrier"

## Recursos Técnicos
- **Q Sharp** (Microsoft) — linguagem para quantum
- **IBM Quantum Experience** — acesso a quantum computers reais (4-5 qubits)
- **Simuladores**: QPython, Quirk

## Questões em Aberto (2026)
- ¿Quantum supremacy foi alcançado? (Google 2019 → Ainda debatido)
- ¿Conseguiremos escalar sem atingir limite físico?
- ¿Topological qubits são viáveis? (Melhor noise resistance)

## Sentimento do Presenter
- Esperançoso sobre potencial
- Nervoso sobre "exponential barrier" — próximos 2 anos são críticos
- Fascinado por entanglement (mais que qualquer outra coisa)

---
**Resumo Executivo**: Tutorial excepcional que trata quantum computing como engenharia, não como magia. Foca em matemática linear + circuitos. Muito mais útil que pop-science.
