#!/usr/bin/env python3
"""
Smart Search Wrapper — Fallback automático Brave → RSS → Web_Fetch
Integrado com OpenClaw web_search tool (retorna JSON)
"""

import json
import sys
import re
from datetime import datetime, timedelta
from pathlib import Path

# Simulado — em produção, chamaria OpenClaw tools diretamente
CACHE_FILE = Path("/home/clopes/.openclaw/workspace/finance/search_cache.json")
RSS_FEEDS = [
    "https://news.ycombinator.com/rss",
    "http://export.arxiv.org/rss/cs.AI",
    "https://www.technologyreview.com/feed/",
    "https://newsletter.semianalysis.com/feed",
]

def load_cache():
    """Carrega cache de pesquisas anteriores."""
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except:
            return {"queries": {}}
    return {"queries": {}}

def save_cache(cache):
    """Guarda cache atualizado."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))

def is_cache_valid(cached_result):
    """Verifica se cache é recente (<24h)."""
    if not cached_result:
        return False
    timestamp = datetime.fromisoformat(cached_result.get("timestamp", "2000-01-01"))
    return datetime.now() - timestamp < timedelta(hours=24)

def smart_search(query, max_results=5):
    """
    Executa pesquisa com fallback automático:
    1. Verifica cache (se válido, retorna)
    2. Tenta Brave Search
    3. Se falhar (429), tenta RSS feeds
    4. Se falhar, tenta web_fetch em sites-chave
    5. Se tudo falhar, retorna vazio
    """
    
    print(f"🔍 Smart Search: '{query}'", file=sys.stderr)
    
    # 1. CACHE CHECK
    cache = load_cache()
    if query in cache["queries"]:
        cached = cache["queries"][query]
        if is_cache_valid(cached):
            print(f"✅ Cache hit (válido há {cached['age']})", file=sys.stderr)
            return cached["results"]
    
    # 2. BRAVE SEARCH
    print("📡 Tentando Brave Search...", file=sys.stderr)
    try:
        # Simulação — em produção seria chamada ao tool web_search diretamente
        # results = call_openclaw_web_search(query, max_results)
        # Por agora, retornamos structure que IA Watch/Super Briefing esperam
        results = {
            "status": "error",
            "code": "RATE_LIMITED"
        }
        
        if results.get("status") == "error":
            raise Exception(f"Brave Error: {results.get('code')}")
        
        # Cache hit bem-sucedido
        cache["queries"][query] = {
            "timestamp": datetime.now().isoformat(),
            "results": results.get("results", []),
            "age": "0m"
        }
        save_cache(cache)
        return results.get("results", [])
        
    except Exception as brave_error:
        print(f"⚠️ Brave falhou: {brave_error}", file=sys.stderr)
    
    # 3. RSS FEEDS FALLBACK
    print("📰 Fallback para RSS feeds...", file=sys.stderr)
    try:
        # Simulação de parse RSS
        rss_results = parse_rss_feeds(query, max_results)
        if rss_results:
            print(f"✅ RSS retornou {len(rss_results)} resultados", file=sys.stderr)
            
            # Cache resultado
            cache["queries"][query] = {
                "timestamp": datetime.now().isoformat(),
                "results": rss_results,
                "age": "0m",
                "source": "RSS"
            }
            save_cache(cache)
            return rss_results
    except Exception as rss_error:
        print(f"⚠️ RSS falhou: {rss_error}", file=sys.stderr)
    
    # 4. WEB_FETCH DIRETO (sites-chave)
    print("🌐 Fallback para web_fetch direto...", file=sys.stderr)
    try:
        fetch_results = fetch_key_sites(query, max_results)
        if fetch_results:
            print(f"✅ Web_fetch retornou {len(fetch_results)} resultados", file=sys.stderr)
            
            # Cache resultado
            cache["queries"][query] = {
                "timestamp": datetime.now().isoformat(),
                "results": fetch_results,
                "age": "0m",
                "source": "Web_Fetch"
            }
            save_cache(cache)
            return fetch_results
    except Exception as fetch_error:
        print(f"⚠️ Web_fetch falhou: {fetch_error}", file=sys.stderr)
    
    # 5. FALHA COMPLETA
    print("❌ Todas as estratégias falharam", file=sys.stderr)
    cache["queries"][query] = {
        "timestamp": datetime.now().isoformat(),
        "results": [],
        "age": "0m",
        "source": "FAILED",
        "error": "All search methods exhausted"
    }
    save_cache(cache)
    return []

def parse_rss_feeds(query, max_results):
    """Parse RSS feeds filtrando por query."""
    results = []
    keywords = query.lower().split()
    
    # Simulação — em produção usaria feedparser
    # Por agora, retorna estrutura esperada
    for feed_url in RSS_FEEDS:
        try:
            # Aqui entraria: feed = feedparser.parse(feed_url)
            # Para agora: simulamos resultado vazio ou dummy
            pass
        except:
            continue
    
    return results[:max_results]

def fetch_key_sites(query, max_results):
    """Web_fetch direto em sites-chave (CNBC, MIT, SemiAnalysis, etc)."""
    sites = [
        "https://www.cnbc.com",
        "https://www.technologyreview.com",
        "https://newsletter.semianalysis.com",
        "https://www.understandingai.org",
    ]
    
    results = []
    
    # Simulação — em produção usaria web_fetch tool
    # for site in sites:
    #     try:
    #         content = call_openclaw_web_fetch(site)
    #         # Parse content para query relevance
    #         results.append(...)
    #     except:
    #         continue
    
    return results[:max_results]

def main():
    if len(sys.argv) < 2:
        print("Uso: python search_wrapper.py <query> [max_results]", file=sys.stderr)
        sys.exit(1)
    
    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    results = smart_search(query, max_results)
    
    # Output JSON para agentTurn processar
    output = {
        "query": query,
        "results_count": len(results),
        "results": results,
        "timestamp": datetime.now().isoformat()
    }
    
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
