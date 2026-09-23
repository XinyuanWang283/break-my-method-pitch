# Break My Method — 5-minute speaker notes

Live demo: https://safe-ship-sidekick.lovable.app/


## 0:00–0:45 · Problem

AI teams ship prompt and model updates constantly. The standard evaluation can stay green while particular user cases get worse. Here is a support-email extractor: it returns an order ID and the requested action. We shortened its production prompt. Both versions still score one hundred percent on our clean examples. The candidate looks safe to ship. But equal clean accuracy does not tell us whether a removed instruction mattered.

Our customer is the AI product or ML engineering team making that release decision. Break My Method asks: what should we test before we ship?



## 0:45–1:20 · Product + Nebius

GPT-OSS-120B on Nebius Token Factory is the live experiment planner. It compares the prompts, sees the remaining test families and budget, and chooses the next test. Then we reveal real, previously executed evidence from the frozen clean audit. Only those revealed scores return to the planner. It never sees scores for unselected families.

The model chooses where to look. It never invents the evidence. The loop stops at a twenty percentage-point regression or after three families. The task-model evidence came from Qwen/Qwen3-30B-A3B-Instruct-2507; GPT-OSS-120B makes the planning decisions.



## 1:20–2:40 · Live demo

Click the title or press D to open the live site in a new tab. Show that clean accuracy is one hundred percent for both versions. Click BREAK MY METHOD once. Read the actual live hypothesis and sequence, then open the evidence. If regression is found, point to V1 forty percent, V2 zero percent, and the forty-point drop. State the actual live test count; do not promise one or two tests.

Return to this deck and advance to Evidence by 2:40. Keep the demo within sixty to ninety seconds. If the service is unavailable or the budget expires, say so and move directly to the separately audited result. Do not present the audit as a live outcome.



## 2:40–3:40 · Evidence

Separate from the live run, we froze both prompts, all examples, the scoring rule and the planner prompt. In three fresh-context runs, Nebius found the hidden regression after two, two and one test families. With one regression family among six, uniform random search without replacement takes three point five tests in expectation. Within two tests, Nebius succeeded in all three audited runs; random search has an exact thirty-three point three percent chance.

The hidden condition is instruction-like customer content: V1 scores forty percent and V2 zero. V1 is not secure; it still fails three of the five examples. This is a small synthetic demonstration, not statistical significance or evidence of general superiority. Random expectation covers the full six-family search; planner runs have a budget of three.

Source: clean audit 20260923T105229532804Z/benchmark.json. The benchmark remains separate from live outcomes.



## 3:40–4:30 · Company / 4:30–5:00 · Close + buffer

Our target customer is the team shipping prompt and model updates. Today, engineers choose regression tests manually, spending engineering time and inference budget. We want to add active test selection on top of their existing evaluation workflows. The proposed business model is a team subscription plus evaluation usage, with private deployment for enterprise teams. That is the commercial direction, not a claim of existing revenue.

Today the working product tests a prompt regression. Models, RAG systems and agents are next. Open weights make it possible for teams to pin and privately deploy a planner, and eventually adapt it to their own regression history. These are future directions, not capabilities we have demonstrated today.

Standard evals tell you what got better. Break My Method finds what got worse before your users do.

Leave the remaining time for the close, a slow demo or questions. Do not add a sixth slide.


