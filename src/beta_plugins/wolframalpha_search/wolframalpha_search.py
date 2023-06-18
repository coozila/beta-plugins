from . import BetaWolframBetaSearch

plugin = BetaWolframBetaSearch()


def _wolframbeta_search(query: str) -> str | list[str]:
    res = ""
    try:
        ans = plugin.api.query(query)
        res = next(ans.results).text
    except Exception as e:
        return f"'_wolframbeta_search' on query: '{query}' raised exception: '{e}'"
    return res
