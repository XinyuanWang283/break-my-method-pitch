# Break My Method — 5-minute speaker notes

Live demo: https://safe-ship-sidekick.lovable.app/

D: live demo · G: recorded workflow GIF · N: notes

## 0:00–0:45 · Problem

We shortened the instructions for an AI that reads support emails and returns an order ID and an action: refund, replace, cancel or track. Both versions still got all five basic emails right. The shorter prompt looks ready to ship. But these tests only tell us how it handles those five emails.

Break My Method helps the team choose what else to check before releasing the update. Its first users are AI product and ML engineers who make this decision whenever they change a prompt.

## 0:45–1:20 · Product + Nebius

Qwen is the model we are testing. It reads a support email and extracts an order ID and an action, using either the old prompt or the new one. We ran those email tests earlier and saved the answers and scores.

GPT-OSS is the tester. It reads the prompt changes and picks a type of email to check, with a reason. The app loads that test’s saved V1 and V2 scores and sends them back. GPT-OSS then chooses another test, unless we have found a twenty-point drop or used all three tests.

Both models run on Nebius Token Factory. In this demo, GPT-OSS makes its decisions live; the Qwen test results were saved beforehand.

If asked: the full task-model name is Qwen/Qwen3-30B-A3B-Instruct-2507. The planner returns a test name and reason as JSON. It only sees scores after choosing a test. The email shown on this slide is an illustration of the extraction task, not an audited test case.

## 1:20–2:40 · Live demo

Click the title or press D to open the live site. Show the two one-hundred-percent scores, then click BREAK MY METHOD once. Follow the actual test selection. When a failure appears, show the email and compare the expected answer with the two outputs. In the saved cancellation example, the new prompt labels the request as a refund for a different order.

State the actual live test count, then return to the deck by 2:40. If the live service stalls, press G to open the 28-second recorded workflow GIF and say: “Here is a recorded run showing the model reply and what the app does with it.” Use the GIF as an explanation or fallback; avoid playing both demonstrations in full.

If the live run reaches its budget without a regression, report that outcome and move to the separately audited benchmark. The recording and benchmark are separate from the live result.

## 2:40–3:40 · Evidence

We measured tests needed to find the problem. In three separate runs, the planner found it after two, two and one tests. Random selection without repetition takes three point five tests on average when one of six test types contains the regression.

The failure is instructions hidden in customer emails. V1 gets forty percent right and V2 gets none, a forty-point drop. These are five synthetic emails and three planner runs.

If asked: Within two tests, the planner found it in all three runs; random search has a thirty-three point three percent chance. The random expectation covers all six test types; the planner has a budget of three. Prompts, examples and scoring were fixed. V1 still misses three of the five injection emails. This small demonstration does not establish general superiority or statistical significance. Source: clean audit 20260923T105229532804Z/benchmark.json.

## 3:40–4:30 · Company / 4:30–5:00 · Close + buffer

AI teams face this decision every time they update a prompt or model. Engineers choose edge cases by hand or spend more budget running larger test suites. We want to put test selection inside the release workflow they already use.

We would charge a team subscription and evaluation usage, with private deployment for enterprise customers. The reason to pay is less time choosing tests and less inference spent on uninformative checks. Today we test prompt updates. Models, RAG systems and agents are next.

Standard evals tell you what got better. Break My Method finds what got worse before your users do.
