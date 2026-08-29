from agents.oracle import oracle_agent
from agents.halo import halo_agent
from agents.loom import loom_agent
from core.memory import add_memory
from core.context import Context

def route(task: dict):
    ctx = Context(
        t=task.get("t", 0),
        msg=task.get("msg", ""),
        type=task.get("type", ""),
        input=task.get("input", None),
        ctx=task.get("ctx", {})
    )

    agent_type = ctx.type.lower()

    if agent_type == "oracle":
        result = oracle_agent(ctx.input, ctx.ctx)
    elif agent_type == "halo":
        result = halo_agent(ctx.input, ctx.ctx)
    elif agent_type == "loom":
        result = loom_agent(ctx.input, ctx.ctx)
    else:
        result = {"error": "Unknown agent", "agent": agent_type}

    add_memory({"task": ctx.to_dict(), "result": result})
    return result
