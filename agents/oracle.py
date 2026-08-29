def oracle_agent(input, ctx):
    return {
        "agent": "oracle",
        "answer": f"Oracle processed: {input}",
        "ctx": ctx
    }
