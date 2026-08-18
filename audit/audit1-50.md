# Audit of `data/comparisons.csv`, rows 1–50

Audited 18 Aug 2026. Every one of the 50 rows was checked against its cited thread on
old.reddit.com (all 7 threads fetched in full, comment trees parsed — author, score,
body, parent chain). For each row: (a) is the quote verbatim from the page? (b) does the
full comment support the coded winner/loser pair? (c) is the comfort axis stated? (d) is
the evidence tag (and thus the weight) actually supported? Where the stored quote is a
fragment, a fuller verbatim quote is proposed; where the pair is not supportable, a
deletion is recommended.

**Verdicts at a glance**

| Verdict | Rows |
|---|---|
| OK — quote verified; fuller quote suggested | 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 20, 21, 22, 23, 26, 27, 30, 33, 35, 37, 39, 40, 41, 42, 43, 44, 46, 48, 49 |
| OK pair, but evidence tag (weight) is wrong | 2, 18, 25, 29, 36, 38, 47, 50 |
| Quote misleading / pair not stated in the quote | 9, 17, 24 |
| **Delete** — pair unsupported by any single comment | **1, 10, 16, 19, 28, 31, 45** |
| Marker / editorial row (harmless, wt=0) | 34 |

Cross-cutting issues (detail at the bottom): several `upvotes` values don't match the
current Reddit score (rows 19, 22, 32, 35, 50 — informational only; upvotes are planned
for removal from all data and calculations); row 33 quotes the **post body**, not a
comment; row 21's author account is deleted; rows 16 and 19's stored quotes contain
**coder editorial text** that is not on the page.

---

## Thread 1 — `1gi84ub` "The most 'comfortable' SUV under 55k" (rows 1–3)

### Row 1 — Lincoln Aviator > Lexus RX · ride · owned_one_td_other · wt 1.5 · up 69 → **DELETE** (or recode)

Stored quote: `genuine perfect vehicle… Lincoln still makes cars that are luxury only, not sporty at all`

Actual comment (u/OverseasonedToyota, 68 pts, top-level):

> "Most would say a Lexus. I'd still agree, but the genuine perfect vehicle in this
> situation is a Lincoln Aviator. Lincoln still makes cars that are luxury only, not
> sporty at all. They still have some power under the hood though. Unfortunately they're
> not the most reliable…"

Problems:
- The sentence the quote is torn from actually **concedes** the Lexus answer ("Most would
  say a Lexus. I'd still agree…"). The comment is a recommendation, not a first-hand
  relative statement — it fails the project's own inclusion rule.
- No ownership or test-drive claim anywhere → `owned_one_td_other` (1.5) is unsupported;
  at best `opinion` (0.7).
- "Luxury only, not sporty" is not an explicit *ride* statement; axis is inferred.

Recommendation: **delete**. Fallback if kept: full quote above, evidence `opinion`,
axis `overall`.

### Row 2 — Lincoln Aviator > Lincoln Corsair · ride · owned_one_td_other · wt 1.5 · up 2 → **KEEP, fix quote + evidence**

Stored quote: `They don't ride as nice, and aren't built as well though`

Actual comment (u/OverseasonedToyota, 1 pt), reply to u/VegaGT-VZ — "I have one- they're
huge. I think one of the smaller cheaper Lincolns would be better for a single person":

> "They don't ride as nice, and aren't built as well though"

- The pair is supportable **only via the parent**: "they" = the smaller cheaper Lincolns
  (Corsair) vs the Aviator the parent owns. The stored quote alone is unintelligible.
- The author never claims ownership → evidence should be `opinion` (or `opinion_plus_drive`),
  not `owned_one_td_other`.

Recommendation: keep, quote = parent + reply combined:
> Parent: "I have one- they're huge. I think one of the smaller cheaper Lincolns would be
> better for a single person." Reply: "They don't ride as nice, and aren't built as well though."

Recode evidence to `opinion`. (Upvotes: stored 2, current 1 — fuzz.)

### Row 3 — Lexus RX > Audi A7 · nvh · owned_both · wt 3.0 · up 3 → **OK**

Stored quote: `I've had a current gen RX and a last gen Audi A7, the Lexus was quieter and more softly sprung`

Actual (u/dmeech999, 2 pts):

> "Body on frame SUVs are worse, crossover SUVs like Lexus RX are very comfy. I've had a
> current gen RX and a last gen Audi A7, the Lexus was quieter and more softly sprung -
> was like being in a bank vault."

Pair ✓, axis (nvh) ✓, `owned_both` ✓ ("I've had a current gen RX and a last gen Audi A7").
Suggest the full quote ending at "bank vault."

---

## Thread 2 — `1opp4z4` "Most comfortable SUV for long drives — CR-V, Outback, or CX-50?" (rows 4–15)

### Row 4 — Volvo XC60 > Mazda CX-5 · seats · owned_both · wt 3.0 · up 9 → **OK**

Stored quote: `Love my CX5, but got a XC-60 last year and that wins hands down… Most comfortable seats I've tried`

Actual (u/Wanderlustification, 9 pts):

> "Love my CX5, but got a XC-60 last year and that wins hands down if you can stretch the
> budget. Most comfortable seats I've tried of any brand."

Pair ✓, axis ✓, `owned_both` ✓. Suggest full quote (the ellipsis drops "if you can
stretch the budget" and "of any brand").

### Rows 5 & 6 — Honda CR-V > Subaru Outback / Mazda CX-50 · overall · test_drove_both · wt 2.0 · up 24 → **OK**

Stored quote (row 5): `It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V Hybrid`
Stored quote (row 6): `It's the CR-V, hands down. We test drove all of these` ← truncated duplicate

Actual (u/AI_Talking_Practice, 24 pts):

> "It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V
> Hybrid, and we've been thrilled."

Both rows derive from this one comment ("all of these" = the three title cars + CX-5).
✓ test_drove_both ✓. **Fix row 6's quote to the same full quote as row 5.**

### Rows 7 & 8 — Subaru Outback > Honda CR-V / Mazda CX-5 · ride · opinion_plus_drive · wt 1.5 · up 2 → **OK**

Stored quote (row 7): `Outback is much more comfortable. Drive the others over a bad road with potholes`
Stored quote (row 8): `Avoid Crv and Mazda. There are plenty of much more comfortable options.`

Actual (u/mgobla, 2 pts):

> "Outback is much more comfortable. Drive the others over a bad road with potholes and
> you will feel the difference. Avoid Crv and Mazda. There are plenty of much more
> comfortable options."

Both rows come from the same comment. Row 8's stored quote is dangling without row 7's
first sentence ("much more comfortable" than what?). Recommendation: **one full quote for
both rows**: the two sentences above. Axis ride ✓ (potholes/bad road). "Mazda" = the
thread's CX-5/CX-50 ✓.

### Row 9 — Subaru Outback 2026 > Mazda CX-50 · seats · test_drove_both · wt 3.0 · up 1 → **KEEP with fixes, or DELETE**

Stored quote: `I tried all the Mazda options and none of them were any better than the Mazda 3 I had I ended up with the 2026 out back and I love it`

Actual (u/bigchief2077, 1 pt), reply to u/sgrbrry ("…Boyfriend is pushing heavily to
'size up' to a CX-30…"):

> "I tried all the Mazda options and none of them were any better than the Mazda 3 I had
> I ended up with the 2026 out back and I love it"

Problems:
- The comment never names the CX-50 (pair relies on thread context — OP's candidates
  were CR-V/Outback/CX-50).
- **No mention of seats** → axis `seats` is invented; the thread theme is long-trip
  comfort.
- `test_drove_both` is off: he "tried" Mazdas but *owns* the Outback → `owned_one_td_other` (1.5).

Recommendation: keep with quote + parent context, recode axis → `overall`, evidence →
`owned_one_td_other`. Or delete under a strict "both models named" rule.

### Row 10 — Honda CR-V > Mazda CX-5 · overall · owned_one_td_other · wt 1.5 · up 1 → **DELETE**

Stored quote: `I say all this as a cx5 owner (i'll be selling it soon)… CRV… is for sure comfy and smooth`

Actual (u/TheOliveYeti, 1 pt):

> "CRV. My mom has one and while it is a little boring for my pretentious taste, it is
> for sure comfy and smooth. I took it on a 9 hour road trip… I say all this as a cx5
> owner (i'll be selling it soon)"

The comment is **isolated praise of the CR-V** (her mom's car) plus a note that the author
owns a CX-5. There is **no relative statement** CR-V vs CX-5 anywhere — exactly what the
methodology says to exclude. The stored quote even omits "My mom has one," which is the
tell. **Delete.**

### Rows 11 & 12 — Toyota Venza > Subaru Outback / Honda CR-V · nvh · owned_one_td_other · wt 1.5 · up 7 → **OK**

Stored quote (row 11): `Venza is a nice blend… seats and road noise are a world of difference if you don't need the trunk space`
Stored quote (row 12): `seats and road noise are a world of difference if you don't need the trunk space of the Outback or crv`

Actual (u/KindTap, 8 pts), reply to "Have a look at the Toyota Venza":

> "For real. Venza is a nice blend of luxury and the seats and road noise are a world of
> difference if you don't need the trunk space of the Outback or crv"

Pair ✓ for both rows, axis nvh ✓ (also seats — fine as one vote). Suggest the full quote
for both rows. Note: no ownership claim by the author → evidence is really `opinion`/
`opinion_plus_drive`; `owned_one_td_other` is not supported. (Upvotes: stored 7, current 8.)

### Rows 13, 14, 15 — BMW X5 > Honda CR-V / Lexus RX / Toyota RAV4 · overall · owned_one_family · wt 1.5 · up 7 → **OK**

Stored quotes: `All of them prefer the X5 if we're together and doing… a longer road trip` /
`My brother has a 2022 RX350… prefer the X5… longer road trip` / `My neighbor has the 2024 RAV4… prefer the X5`

Actual (u/Duckysawus, 6 pts):

> "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has
> the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're
> together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are
> going out together with 3 in the backseat."

All three pairs ✓ from one comment. Suggest **one full quote for rows 13–15** (the final
paragraph above). `owned_one_family` is defensible (the author's X5 + family/neighbor
cars).

---

## Thread 3 — `1kipn8g` "Most comfortable small to midsize SUV for a retired grandma…" (rows 16–19)

OP's post lists the actual candidates: **Cadillac XT5 (mom leaning), Lexus RX, Genesis
GV70/GV80, Lincoln Corsair, Lincoln Nautilus**. RAV4 is not a candidate.

### Row 16 — Lexus RX > Cadillac XT5 · ride · owned_one_td_other · wt 1.5 · up 5 → **DELETE**

Stored quote: `for your mom, I think the RX would be better (vs XC60 harsher; XT5 called lazy)`

This quote **does not exist on the page**. It is a coder composite: the first part is from
u/hotdogspicklechip's comment, and "(XT5 called lazy)" is an editorial note referring to a
*different* commenter's remark (mgobla's, used in row 17). The actual comment chain:

> u/Glarmj: "Volvo XC40/XC60. Most comfortable seats on the market."
> → u/rao-blackwell-ized: "…don't Volvos have harsher suspensions these days…?"
> → u/hotdogspicklechip (4 pts): "Yes. I love my XC60, but for your mom, I think the RX
> would be better."

- The comment compares **RX vs XC60**, not RX vs XT5.
- No comment in the whole thread mentions both RX and XT5, so the pair RX > XT5 is
  unsupported by any single source. **Delete.** (If the RX-vs-XC60 signal is wanted, that
  would be a *new* row, not this one.)

### Row 17 — Lincoln Nautilus > Cadillac XT5 · ride · opinion_plus_drive · wt 1.5 · up 18 → **KEEP, fuller quote**

Stored quote: `XT5 is a lazy money grab… Look for… Lincoln NAUTILUS - Nautilus has a soft suspension tune`

Actual (u/mgobla, 19 pts):

> "XT5 is a lazy money grab by GM, it doesn't ride as well as you might expect. …
> Look for and test drive a USED (high initial depreciation) 2024 model year Lincoln
> NAUTILUS - Nautilus has a soft suspension tune"

Both cars are named in one comment; Nautilus > XT5 on ride is a fair reading (XT5 "doesn't
ride as well as you might expect" vs Nautilus "soft suspension tune"), though it's an
implied comparison, not a single sentence. Suggest the fuller quote above. (Upvotes:
stored 18, current 19.)

### Row 18 — Lexus RX > Lexus NX · ride · owned_one_td_other · wt 1.5 · up 2 → **KEEP, fix evidence**

Stored quote: `RX definitely has a better ride. Longer wheelbase… NX suffers from being the luxury version of a RAV4`

Actual (u/Calm_Strawberry_3478, 3 pts):

> "RX definitely has a better ride. Longer wheelbase means it takes the road better.
> Unfortunately the NX suffers from being the luxury version of a RAV4."

Pair ✓, axis ride ✓. But no ownership or drive claim by this author (the parent only says
"I owned a Mercedes at one point") → evidence should be `opinion`. Suggest the full quote.

### Row 19 — Lexus RX > Toyota RAV4 · overall · owned_one_td_other · wt 1.5 · up 1 → **DELETE**

Stored quote: `She only cares about comfort so you recommend one of the least comfortable… 😭`

Actual (u/skinnyonskin, 3 pts), reply to u/Biobizlab ("Go with a new rav4… these were the 2
things that made Rav4 superior to everything else we looked at for my dad"):

> "She only cares about comfort so you recommend one of the least comfortable and non
> luxurious vehicles you can get 😭😭"

The comment is an **anti-RAV4 jab only — "RX" appears nowhere**, and the RAV4 wasn't even
among the OP's candidates. The pair RX > RAV4 is the coder's invention. **Delete.**

---

## Thread 4 — `1nejfj3` "Absolute MOST comfortable crossover SUV? Is an xc60 the answer?" (rows 20–32)

### Row 20 — Volvo XC60 > Toyota RAV4 · seats · owned_both · wt 3.0 · up 31 → **OK**

Stored quote: `I went from rav4 to an xc60. I could never get comfortable in the rav… Can drive the volvo all day`

Actual (u/NothingLift, 32 pts):

> "I went from rav4 to an xc60. I could never get comfortable in the rav and after an hour
> I was over it. Can drive the volvo all day with no discomfort. The interior and sound
> system are also great, perfect road trip car except the lack of spare tire in the phev
> models. Also the seats are firm but ergonomic…"

Pair ✓, `owned_both` ✓. Suggest the full quote (up to "no discomfort" is enough).

### Row 21 — Volvo XC60 > Toyota RAV4 · seats · owned_both · wt 3.0 · up 9 → **OK** (author deleted)

Stored quote: `Have had a RAV4 for 7 years… XC60… most comfortable car I have driven… she drives it far more than her Rav4 now`

Found in the page (author account now deleted, u/ndph1jj, 10 pts):

> "Oh cool, a post I can actually chime in on! Have had a RAV4 for 7 years now with my
> wife, and it's great. … Tried a 2023 XC60 Plus Bright Theme, and I immediately knew it
> was the right choice. It is undoubtedly the most comfortable car I have driven in thus
> far and can drive long periods without any discomfort. … We are incredibly happy with
> it, and despite her trying to pretend otherwise, she drives it far more than her Rav4 now."

Quote verified as a faithful compression ✓; pair ✓, `owned_both` ✓. Suggest the fuller
quote. (Upvotes: stored 9, current 10.)

### Row 22 — Volvo XC60 > Mazda CX-50 · seats · owned_one_rode_other · wt 1.5 · up 3 → **OK**

Stored quote: `they weren't bad imo. Not as comfortable as our xc60 Volvos`

Actual (u/BulkyBoy808, 1 pt):

> "…2 of my friends have them and I've ridden in both (cx50) and they weren't bad imo.
> Not as comfortable as our xc60 Volvos or GMC Sierra."

Pair ✓, axis ✓, `owned_one_rode_other` ✓ (owns XC60s, rode friends' CX-50s). Suggest the
full sentence incl. "or GMC Sierra". (Upvotes: stored 3, current 1.)

### Row 23 — Volvo XC60 > BMW X3 · seats · test_drove_both · wt 1.5 · up 5 → **OK**

Stored quote: `The Volvo is more comfortable but the BMW infotainment was much better`

Actual (u/YouMeAndReneDupree, 6 pts):

> "When I looked, it was between this and the BMW X1/X3. Both better than the Rav. The
> Volvo is more comfortable but the BMW infotainment was much better. I leaned more
> towards BMW but try it out yourself."

Pair ✓ (XC60 vs X1/X3; X3 coded), axis seats ✓ (thread context), evidence plausible.
Suggest the fuller quote, which is what makes "the Volvo" = XC60 and "the BMW" = X3.

### Row 24 — Audi Q5 > Volvo XC60 · ride · test_drove_both · wt 2.0 · up 4 → **KEEP, fix quote (currently misleading)**

Stored quote: `When I test drove the XC60… it rode like shit… The Q5 is definitely firmer than I think a crossover should be`

Actual (u/lolpandabearz, 3 pts):

> "Just bought a Q5, both seat options are nice… The Volvo seats were slightly better than
> the Audi. When I test drove the XC60 i think it either had 20" wheels or run flats
> because it rode like shit. Small bumps were fine but bigger bumps and pot holes felt
> worse than in my GTI… The Q5 is definitely firmer than I think a crossover should be but
> it drives like a normal car and feels much better to drive than the XC60…"

As stored, the quote's second clause ("Q5 is definitely firmer") cuts **against** the
coded winner and the decisive clause ("feels much better to drive than the XC60") is
omitted. The vote is defensible but the quote must be honest: use the full text above and
note the caveats (XC60 ride complaint tied to wheel spec; Volvo seats judged better).

### Row 25 — Audi Q5 > Volvo XC60 · seats · test_drove_both · wt 2.0 · up 11 → **KEEP, fix evidence**

Stored quote: `I have friends that have both the Q5 and the Volvo and the Q5 seats are really, really comfortable, more so in my opinion than the XC60`

Actual (u/stonewall993, 12 pts):

> "Honestly I would look at the Audi Q5. I have friends that have both the Q5 and the
> Volvo and the Q5 seats are really, really comfortable, more so in my opinion than the
> XC60. …"

Pair ✓, axis seats ✓ — but the author **never drove either car**; friends own them.
`test_drove_both` (2.0) is wrong → `opinion` (0.7) or `opinion_plus_drive` (1.2).

### Rows 26 & 27 — Porsche Macan > Volvo XC60 / Audi Q5 > Volvo XC60 · ride · test_drove_both · wt 2.0 · up 2 → **OK**

Stored quote (both rows): `air suspension optioned Macan and Q5 were way more comfortable ride wise than the XC60`

Actual (u/JimmyGodoppolo, 2 pts):

> "The xc60 for having such good NVH and seats does not have super soft suspension. I
> found that the air suspension optioned Macan and Q5 were way more comfortable ride wise
> than the XC60, especially the Macan since they offer 14 and 18 way adjustable seats."

Both pairs ✓ from one comment. Suggest the full quote for both rows. Note the comparison
is **air-suspension-optioned** Macan/Q5 vs (presumably standard) XC60 — a spec caveat
worth keeping in the quote.

### Row 28 — Mercedes GLC > Volvo XC60 · overall · owned_both · wt 1.5 · up 3 → **DELETE**

Stored quote: `For me, Mercedes GLC is the most comfortable. I had a Volvo wagon… Mercedes is better`

Actual (u/First-County-4667, 4 pts):

> "For me, Mercedes GLC is the most comfortable. I had a Volvo wagon and it was great,
> but the Mercedes is better."

The comment compares the GLC with a **Volvo wagon (V60/V90)** — the XC60 is never named.
The ellipsis in the stored quote hides exactly that. Coding this as GLC > XC60
misidentifies the rival model; `owned_both` is also wrong (the author never owned an
XC60). **Delete** (row 29 already covers GLC vs XC60 from a direct statement).

### Row 29 — Mercedes GLC > Volvo XC60 · overall · opinion_plus_drive · wt 1.5 · up 2 → **KEEP, fix evidence**

Stored quote: `Benz GLC > XC60 at that price range every day of the week`

Actual (u/Beef_Candy, 2 pts):

> "Benz GLC > XC60 at that price range every day of the week. Bonus points for a used
> Porsche Macan"

Direct pair ✓, direction unambiguous. No test-drive claim → evidence `opinion`, not
`opinion_plus_drive`.

### Row 30 — Volkswagen Tiguan > Toyota RAV4 · overall · test_drove_both · wt 2.0 · up 4 → **OK**

Stored quote: `test drove 8 different vehicles in the RAV4 size category… Tiguan to be the most comfortable by far`

Actual (u/HavelkaHome, 4 pts):

> "My wife and I recently test drove 8 different vehicles in the RAV4 size category. My
> whole family found the new Tiguan to be the most comfortable by far. VW wasn't on our
> short list, but the interior sold us."

Pair ✓ (Tiguan best of 8 incl. RAV4-class cars), evidence ✓. Suggest the full quote.

### Row 31 — Lincoln Nautilus > Volvo XC60 · ride · opinion_plus_drive · wt 1.5 · up 10 → **DELETE** (or keep as implied, with context)

Stored quote: `If you want comfort in a RAV4 sized vehicle I'd test drive a Lincoln Nautilus. Lincoln suspensions… softness over handling`

Actual (u/FordF150ChicagoFan, 9 pts), reply to an XC60 owner's comfort praise:

> "If you want comfort in a RAV4 sized vehicle I'd test drive a Lincoln Nautilus. Lincoln
> suspensions and interiors are still designed for softness over handling/grip."

The comment is a **counter-recommendation in reply to an XC60 endorsement**; the Nautilus
vs XC60 comparison is entirely implicit — no relative statement exists. Under the
project's inclusion rule this should be **deleted**. Fallback: keep with the full quote +
the parent (u/OgreMk5's XC60 praise) noted as context, evidence `opinion`.

### Row 32 — Volvo XC60 > Lexus RX · overall · opinion · wt 1.0 · up 0 → **OK**

Stored quote: `The rx is not even on the same spectrum as the Volvo`

Actual (u/chaser2410, 3 pts), reply to u/SnooLobsters6880 ("At different price points /
Xc60 / Lexus Rx / Toyota crown signia"):

> "The rx is not even on the same spectrum as the Volvo"

Pair ✓ in context, `opinion` ✓. Suggest storing quote + parent line. (Upvotes: stored 0,
current 3 — see notes.)

---

## Thread 5 — `1fxpil5` "Most Comfortable Luxury SUV? Mercedes or No?" (rows 33–38)

### Row 33 — Range Rover Sport > Porsche Cayenne · ride · test_drove_both · wt 2.0 · up 0 → **OK — but it quotes the POST BODY, not a comment**

Stored quote: `2024-Range Rover Sport - … the SUV drives like a dream vs Cayenne too sporty`

Actual source — the OP's (u/Firegrlnikki) post body, "I've test drove a few cars and here's what what":

> "2023 Porsche Cayenne- Too Sporty- felt the road too much, love the look but the ride is
> far too uncomfortable. 2024-Range Rover Sport - Don't like how the outside looks, the
> SUV drives like a dream- I test drove it just because I was curious but with the horror
> stories about range rovers - I'll pass"

Pair ✓ (OP test-drove both), axis ride ✓. The stored quote splices two lines of the post;
suggest the full two-line quote above. Note the OP's final picks (Cayenne **with air
suspension**, Q8) — see row 34. `upvotes` is stored as 0 although the post scores 32; if
post-body rows carry a karma field it should be the post score.

### Row 34 — Porsche Cayenne > Porsche Cayenne · exclude · wt 0 · up 0 → **OK as a marker; not a quote**

Stored "quote": `dropped: Cayenne-with-air vs Cayenne-without-air is the same nameplate`

This is an editorial exclusion marker (winner == loser), not page text. It's harmless
(wt=0, evidence=exclude, dropped by rank.py). Suggestion: move this text out of the
`quote` column into a notes field so quote columns stay verbatim-only.

### Row 35 — Mercedes GLE > Lexus GX · ride · owned_both · wt 3.0 · up 4 → **OK**

Stored quote: `I have a 19 Lexus GX and my wife has a 14 mercedes ml350, and the benz wins in the luxury ride and comfort hands down`

Actual (u/Mountain_Cucumber_88, 6 pts):

> "Not sure about the newer mercedes, but I have a 19 Lexus GX and my wife has a 14
> mercedes ml350, and the benz wins in the luxury ride and comfort hands down. In
> fairness, the lexus is an old fashion body on frame and way more capable offroad, but
> for long trips the merc is the clear winner."

Pair ✓ (ML350 = GLE predecessor), `owned_both` ✓. Suggest the full quote. (Upvotes:
stored 4, current 6.)

### Row 36 — Lincoln Aviator > BMW X5 · seats · opinion_plus_drive · wt 1.5 · up 3 → **KEEP, fix evidence + add chain**

Stored quote: `Lincoln would like a word. Their seats absolutely blow the BMW seats away`

Actual (u/Beef_Candy, 4 pts), chain:
u/kosmonavt66 "You should test drive a Volvo XC90." → u/oldmanlook_mylife "Especially with
the X5's multi-contour seat option: [marketing copy]" → u/lyingdogfacepony66 "That seat is
the bomb. You can make it a Lazy Boy on the road. Best car seat ever" → u/Beef_Candy:

> "Lincoln would like a word. Their seats absolutely blow the BMW seats away."

Pair ✓ — "the BMW" is the X5 via the grandparent chain — but that chain is needed, and
"Lincoln" = Aviator comes from the thread's Aviator recommendations. No drive/ownership
claim → evidence `opinion`, not `opinion_plus_drive`.

### Row 37 — BMW X7 > BMW X5 · ride · owned_both · wt 3.0 · up 3 → **KEEP, fix evidence**

Stored quote: `The longer wheel base and air suspension made the X7 feel like you were driving on a cloud, but the X5 was plenty good enough`

Actual (u/Proper-Print-9505, 4 pts):

> "The X7 is my wife's car. I drive a 2018 Audi A4 manual transmission. We did not test
> drive the X6. The longer wheel base and air suspension made the X7 feel like you were
> driving on a cloud, but the X5 was plenty good enough."

Pair ✓, axis ride ✓. But ownership: X7 is the wife's; the commenter drives an A4; the
X5's ownership/test-drive basis is unclear → `owned_both` is shaky; `owned_one_td_other`
or `opinion_plus_drive` is safer. Suggest the full quote.

### Row 38 — Audi Q7 > Audi Q8 · ride · test_drove_both · wt 1.5 · up 1 → **KEEP, fix evidence**

Stored quote: `If sticking with gas, I think the Q7 rides better than the gas Q8`

Actual (u/Far_Effect_3881, 1 pt):

> "Q8 etron if you're OK with electric. The comfort it provides is exactly what you want.
> If sticking with gas, I think the Q7 rides better than the gas Q8."

Pair ✓ (gas versions), axis ride ✓. No test-drive claim → evidence `opinion`. Suggest the
full quote.

---

## Thread 6 — `1khcp25` r/BMWX5 "How do you feel about the GLE compared to the X5?" (rows 39–49)

### Row 39 — Mercedes GLE > BMW X5 · ride · owned_both · wt 3.0 · up 1 → **OK**

Stored quote: `The GLE is a dramatically smoother ride and is my choice for a road trip`

Actual (u/txtbook, 1 pt):

> "I own a 2022 GLE 450 and a 2025 x5 m60i. The GLE is a dramatically smoother ride and is
> my choice for a road trip, despite having only 1 inch smaller wheels and having the base
> suspension. … The ride [of the X5] is much rougher than I was expecting…"

Pair ✓, `owned_both` ✓. Suggest the fuller quote.

### Row 40 — Mercedes GLE > BMW X5 · ride · owned_both · wt 3.0 · up 1 → **OK**

Stored quote: `Mercedes is larger and more comfortable on longer trips`

Actual (u/Petetarga, 1 pt):

> "I have both cars. I drive X5 hybrid and my wife has GLE 350. I think the X5 has better
> engine performance/ response and maneuvering. But Mercedes is larger and more
> comfortable on longer trips."

✓ ✓ ✓. Suggest the fuller quote.

### Row 41 — Mercedes GLE > BMW X5 · ride · owned_both · **wt 1.5 (should be 3.0)** · up 1 → **OK, flag weight**

Stored quote: `The X5 is more fun to drive… the Benz has… plusher and smoother drive for road trips`

Actual (u/aurilovesbirds, 1 pt):

> "Had a GLE and loved it so much that we upgraded to the GLS when we had our second kid.
> Also have an X5. Love both cars. The X5 is more fun to drive for sure but the Benz has
> better technology in my opinion, especially the touchscreen. It is a plusher and
> smoother drive for road trips."

Pair ✓, `owned_both` ✓ — but `weight_base` is 1.5 while every other `owned_both` row is
3.0. rank.py recomputes from the evidence tag, so this only matters if `weight_base` is
used anywhere; still, fix for consistency.

### Row 42 — Mercedes GLE > BMW X5 · ride · owned_both · wt 3.0 · up 1 → **OK**

Stored quote: `GLE is better for road-trips ngl and the x5 better to daily`

Actual (u/atxtony23, 1 pt): "Have both, GLE is better for road-trips ngl and the x5 better
to daily and drive harder." ✓ verbatim, `owned_both` ✓ ("Have both").

### Row 43 — Mercedes GLE > BMW X5 · nvh · test_drove_both · wt 2.0 · up 1 → **OK**

Stored quote: `the merc seemed quieter and smoother to drive`

Actual (u/muchtoes, 1 pt):

> "I was pretty torn between the 2 and ended up buying the X5. The merc seemed quieter
> and smoother to drive but also lacked anything that I would consider fun. I was in the 4
> cylinder 350 though. … The bmw just felt much more connected to the road…"

Pair ✓, axis nvh ✓ ("quieter"), evidence ✓. Suggest the fuller quote; note the 350-engine
caveat.

### Row 44 — BMW X5 > Mercedes GLE · ride · test_drove_both · wt 2.0 · up 1 → **OK**

Stored quote: `X5 is still a smoother ride… the seats in the GLE were uncomfortable`

Actual (u/Marre313, 1 pt): "Test drive both. X5 is still a smoother ride. Not sure what
the exact problem was, but the seats in the GLE were uncomfortable. …" ✓ verbatim.

### Row 45 — BMW X5 > Mercedes GLE · overall · test_drove_both · wt 1.0 · up 1 → **DELETE**

Stored quote: `Bmw is more comfortable... Really...`

Actual (u/brunoc2222, 2 pts, top-level, **0 replies**): the complete comment is exactly
"Bmw is more comfortable... Really..." — nothing else exists on the page.

- Six words, no context, no replies, no parent. In a r/BMWX5 thread it reads as either a
  flat assertion or **sarcastic disbelief** ("…Really?") aimed at the thread premise; the
  trailing ellipsis plus "Really" tilts toward sarcasm/ambiguity.
- `test_drove_both` is unsupported by any text.

**Delete** — an ambiguous 6-word comment cannot carry a coded vote.

### Row 46 — Mercedes GLE > BMW X5 · seats · owned_both · wt 3.0 · up 2 → **OK**

Stored quote: `I do miss the merc seats… Felt the Benz seats were buttery and plush`

Actual (u/773badger, 2 pts):

> "I have had both and currently have the X5. … I do miss the merc seats but the BMW are
> nice too. Felt the Benz seats were buttery and plush. Space in the rear - Benz is bigger
> for 2nd row and cargo."

Pair ✓, axis seats ✓, `owned_both` ✓. Suggest the fuller quote.

### Row 47 — BMW X5 > Mercedes GLE · seats · test_drove_both · wt 2.0 · up 1 → **KEEP, fix evidence**

Stored quote: `My seats are absolutely more comfortable than the GLE, even as a bigger dude`

Actual (u/x1tyrant1x, 2 pts):

> "The X5 fit and finish feels more refined, IMHO. The GLE felt more toyish to me… My
> seats are absolutely more comfortable than the GLE, even as a bigger dude. Mercedes
> does have nice air suspension, but you can get that in the X5 too. I personally stuck w
> the dynamic suspension on the X5…"

Pair ✓, axis ✓. But "My seats" = the author **owns** the X5; no test-drive claim →
evidence `owned_one_td_other` (or plain opinion if the GLE exposure was a showroom sit).

### Rows 48 & 49 — BMW X5 > Mercedes GLE / Porsche Cayenne · seats · test_drove_both · wt 2.0 · up 0 → **OK**

Stored quote (48): `with the inexpensive Multi contour seats option, the X5 seats are more comfortable… including the highest end Cayenne seats`
Stored quote (49): `X5 seats are more comfortable and adjustable than anything else I tried, including the highest end Cayenne seats`

Actual (u/fiddly-bits, 1 pt):

> "I'm not a BMW guy. This X5 is my first one. I test drove all the foreign luxury mid
> size SUVs with an open mind. … That said, with the inexpensive Multi contour seats
> option, the X5 seats are more comfortable and adjustable than anything else I tried,
> including the highest end Cayenne seats. The Merc seats are ok, but nothing special in
> the segment."

Both pairs ✓ from one comment; evidence ✓ ("test drove all the foreign luxury mid size
SUVs"). Suggest one fuller quote for both rows.

---

## Thread 7 — `1mbg5ci` "What is the most comfortable SUV or Sedan you drove/rode in your life?" (row 50)

### Row 50 — BMW X5 > Mercedes GLE · ride · **test_drove_both (should be owned_both)** · wt 3.0 · up 21 → **KEEP, fix evidence**

Stored quote: `X5 air suspension… We had a MB GLE350 for 3 years and it was too bouncy… traded… X5 M60i`

Actual (u/the_robmeister_, **10 pts**):

> "Under $150k in current market, I would argue the most comfortable SUV I have driven
> thus far is a 2025 BMW X5 with the adjustable air suspension. We had a MB GLE350 for 3
> years and it was too bouncy and lacked power when you needed it most. We traded that
> car in for the X5 M60i and I can't tell you how many good things there are for that
> car…"

Pair ✓, axis ride ✓. The commenter **owned both** (GLE 3 years, traded for X5) →
evidence `owned_both`, not `test_drove_both` (the stored wt 3.0 is right; the tag is
wrong — matters for the owners-only fit, where `test_drove_both` is dropped).
**Upvotes: stored 21, current score 10** — the largest discrepancy in the batch; a
non-issue given the planned removal of upvotes from all data and calculations (see
notes). Suggest the fuller quote.

---

## Cross-cutting notes

1. **`upvotes` column is unreliable for several rows (non-issue — planned for removal).**
   Current Reddit scores vs stored:
   row 19 (stored 1, now 3), row 22 (3 → 1), row 32 (0 → 3), row 35 (4 → 6), row 50
   (21 → 10). ±1 elsewhere (rows 1, 2, 3, 11, 12, 13–15, 16, 18, 20, 21, 23, 24, 25, 28,
   31, 36, 37, 45, 47, 48, 49). Were the column still live, a 21-vs-10 error would
   change row 50's karma multiplier by ~25%, and 0-vs-3 would change row 32 from no
   boost to a 1.39× boost. **However, upvotes are planned to be removed from all data
   and calculations** (the `upvotes` column and the `log(1+upvotes)` karma multiplier),
   so these values are legacy — do not re-capture them.

2. **Stored quotes contain coder editorial text in rows 16 and 19** ("(vs XC60 harsher;
   XT5 called lazy)" and the 😭 row). The `quote` column should be verbatim source text
   only; editorial notes belong in a separate column. Row 34's "quote" is likewise an
   editorial marker.

3. **Row 33 quotes the post body**, not a comment — fine as a source, but note that
   `upvotes` can't be a comment score there (post scores 32); decide a convention for
   OP-writeup rows.

4. **Evidence-tag errors change weights in all three fits** (rank.py derives weight from
   the evidence tag: owned_both 3.0, test_drove_both 2.0, owned_*/opinion_plus_drive
   1.2–1.5, opinion 0.7). Rows needing tag fixes: 2, 18, 25, 29, 36, 37, 38, 47, 50.
   The owners-only fit additionally drops `test_drove_both`, so row 50 currently gets
   dropped there despite being a genuine owned-both statement.

5. **Row 41's `weight_base` (1.5) contradicts its `owned_both` evidence (3.0)** — and
   row 24's `test_drove_both` (2.0) is arguably `owned_one_td_other` (1.5) since the
   author bought the Q5. `weight_base` is not used by rank.py, but the column should be
   consistent for downstream readers.

6. **Rows 34's pair (Cayenne > Cayenne) and row 9's "2026 out back" typo** (source's
   own typo, fine) are noted for completeness.

### Bottom line

- **Delete 7 rows:** 1, 10, 16, 19, 28, 31, 45 (pair not supported by any single
  comment, or model misidentified, or text ambiguous).
- **Fix quotes on ~10 rows** (5/6 unify, 7/8 unify, 13–15 unify, 17, 24, 33, plus the
  full-quote suggestions in the OK rows).
- **Fix evidence tags on 9 rows:** 2, 18, 25, 29, 36, 37, 38, 47, 50.
- **Upvotes: no action.** The `upvotes` column and the `log(1+upvotes)` karma
  multiplier are planned to be removed from all data and calculations; the drift
  seen in rows 19, 22, 32, 35, 50 is a non-issue and should not be re-captured.
