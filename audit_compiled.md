# audit_compiled — one line per suggested change
Each line: `<id> <TAG>: <winner> > <loser> — <action>`; id = report number = CSV id column. Tags: OK keep / QUOTE_FIX replace quote / RECODE change field / DELETE remove row / UNVERIFIED re-audit when fetchable. Upvotes intentionally untouched (planned for removal).
1 DELETE: Lincoln Aviator > Lexus RX — remove row
2 QUOTE_FIX: Lincoln Aviator > Lincoln Corsair — add parent/thread context: "I have one- they're huge. I think one of the smaller cheaper Lincolns would be better for a single person. They don't ride as nice, and aren't built as well though."
2 RECODE: Lincoln Aviator > Lincoln Corsair — evidence owned_one_td_other → opinion
3 OK: Lexus RX > Audi A7 — keep as-is; fuller quote suggested: "I've had a current gen RX and a last gen Audi A7, the Lexus was quieter and more softly sprung - was like being in a bank vault."
4 OK: Volvo XC60 > Mazda CX-5 — keep as-is; fuller quote suggested: "Love my CX5, but got a XC-60 last year and that wins hands down if you can stretch the budget. Most comfortable seats I've tried of any brand."
5 OK: Honda CR-V > Subaru Outback — keep as-is; fuller quote suggested: "It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V Hybrid, and we've been thrilled."
6 QUOTE_FIX: Honda CR-V > Mazda CX-50 — replace quote with: "It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V Hybrid, and we've been thrilled."
7 OK: Subaru Outback > Honda CR-V — keep as-is; fuller quote suggested: "Outback is much more comfortable. Drive the others over a bad road with potholes and you will feel the difference. Avoid Crv and Mazda. There are plenty of much more comfortable options."
8 OK: Subaru Outback > Mazda CX-5 — keep as-is; fuller quote suggested: "Outback is much more comfortable. Drive the others over a bad road with potholes and you will feel the difference. Avoid Crv and Mazda. There are plenty of much more comfortable options."
9 QUOTE_FIX: Subaru Outback 2026 > Mazda CX-50 — add parent/thread context: "…Boyfriend is pushing heavily to 'size up' to a CX-30…"
9 RECODE: Subaru Outback 2026 > Mazda CX-50 — axis seats → overall
9 RECODE: Subaru Outback 2026 > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
10 DELETE: Honda CR-V > Mazda CX-5 — remove row
11 OK: Toyota Venza > Subaru Outback — keep as-is; fuller quote suggested: "For real. Venza is a nice blend of luxury and the seats and road noise are a world of difference if you don't need the trunk space of the Outback or crv"
12 OK: Toyota Venza > Honda CR-V — keep as-is; fuller quote suggested: "For real. Venza is a nice blend of luxury and the seats and road noise are a world of difference if you don't need the trunk space of the Outback or crv"
13 OK: BMW X5 > Honda CR-V — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
14 OK: BMW X5 > Lexus RX — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
15 OK: BMW X5 > Toyota RAV4 — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
16 DELETE: Lexus RX > Cadillac XT5 — remove row
17 QUOTE_FIX: Lincoln Nautilus > Cadillac XT5 — replace quote with: "XT5 is a lazy money grab by GM, it doesn't ride as well as you might expect. … Look for and test drive a USED (high initial depreciation) 2024 model year Lincoln NAUTILUS - Nautilus has a soft suspension tune"
18 RECODE: Lexus RX > Lexus NX — evidence owned_one_td_other → opinion
19 DELETE: Lexus RX > Toyota RAV4 — remove row
20 OK: Volvo XC60 > Toyota RAV4 — keep as-is; fuller quote suggested: "I went from rav4 to an xc60. I could never get comfortable in the rav and after an hour I was over it. Can drive the volvo all day with no discomfort."
21 OK: Volvo XC60 > Toyota RAV4 — keep as-is; fuller quote suggested: "Oh cool, a post I can actually chime in on! Have had a RAV4 for 7 years now with my wife, and it's great. … Tried a 2023 XC60 Plus Bright Theme, and I immediately knew it was the right choice. It is undoubtedly the most comfortable car I have driven in thus far and can drive long periods without any discomfort. … We are incredibly happy with it, and despite her trying to pretend otherwise, she drives it far more than her Rav4 now."
22 OK: Volvo XC60 > Mazda CX-50 — keep as-is; fuller quote suggested: "…2 of my friends have them and I've ridden in both (cx50) and they weren't bad imo. Not as comfortable as our xc60 Volvos or GMC Sierra."
23 OK: Volvo XC60 > BMW X3 — keep as-is; fuller quote suggested: "When I looked, it was between this and the BMW X1/X3. Both better than the Rav. The Volvo is more comfortable but the BMW infotainment was much better. I leaned more towards BMW but try it out yourself."
24 QUOTE_FIX: Audi Q5 > Volvo XC60 — replace quote with: "Just bought a Q5, both seat options are nice… The Volvo seats were slightly better than the Audi. When I test drove the XC60 i think it either had 20" wheels or run flats because it rode like shit. Small bumps were fine but bigger bumps and pot holes felt worse than in my GTI… The Q5 is definitely firmer than I think a crossover should be but it drives like a normal car and feels much better to drive than the XC60…"
25 RECODE: Audi Q5 > Volvo XC60 — evidence test_drove_both → opinion
26 OK: Porsche Macan > Volvo XC60 — keep as-is; fuller quote suggested: "The xc60 for having such good NVH and seats does not have super soft suspension. I found that the air suspension optioned Macan and Q5 were way more comfortable ride wise than the XC60, especially the Macan since they offer 14 and 18 way adjustable seats."
27 OK: Audi Q5 > Volvo XC60 — keep as-is; fuller quote suggested: "The xc60 for having such good NVH and seats does not have super soft suspension. I found that the air suspension optioned Macan and Q5 were way more comfortable ride wise than the XC60, especially the Macan since they offer 14 and 18 way adjustable seats."
28 DELETE: Mercedes GLC > Volvo XC60 — remove row
29 RECODE: Mercedes GLC > Volvo XC60 — evidence opinion_plus_drive → opinion
30 OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is; fuller quote suggested: "My wife and I recently test drove 8 different vehicles in the RAV4 size category. My whole family found the new Tiguan to be the most comfortable by far. VW wasn't on our short list, but the interior sold us."
31 DELETE: Lincoln Nautilus > Volvo XC60 — remove row
32 OK: Volvo XC60 > Lexus RX — keep as-is; fuller quote suggested: "At different price points / Xc60 / Lexus Rx / Toyota crown signia. The rx is not even on the same spectrum as the Volvo"
33 OK: Range Rover Sport > Porsche Cayenne — keep as-is; fuller quote suggested: "2023 Porsche Cayenne- Too Sporty- felt the road too much, love the look but the ride is far too uncomfortable. 2024-Range Rover Sport - Don't like how the outside looks, the SUV drives like a dream- I test drove it just because I was curious but with the horror stories about range rovers - I'll pass"
34 OK: Porsche Cayenne > Porsche Cayenne — keep as-is; editorial exclusion marker (wt=0); optionally move marker text out of quote column
35 OK: Mercedes GLE > Lexus GX — keep as-is; fuller quote suggested: "Not sure about the newer mercedes, but I have a 19 Lexus GX and my wife has a 14 mercedes ml350, and the benz wins in the luxury ride and comfort hands down. In fairness, the lexus is an old fashion body on frame and way more capable offroad, but for long trips the merc is the clear winner."
36 RECODE: Lincoln Aviator > BMW X5 — evidence opinion_plus_drive → opinion
36 QUOTE_FIX: Lincoln Aviator > BMW X5 — add parent/thread context: "You should test drive a Volvo XC90. Especially with the X5's multi-contour seat option: [marketing copy]. That seat is the bomb. You can make it a Lazy Boy on the road. Best car seat ever"
37 RECODE: BMW X7 > BMW X5 — evidence owned_both → owned_one_td_other
38 RECODE: Audi Q7 > Audi Q8 — evidence test_drove_both → opinion
39 OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I own a 2022 GLE 450 and a 2025 x5 m60i. The GLE is a dramatically smoother ride and is my choice for a road trip, despite having only 1 inch smaller wheels and having the base suspension. … The ride [of the X5] is much rougher than I was expecting…"
40 OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I have both cars. I drive X5 hybrid and my wife has GLE 350. I think the X5 has better engine performance/ response and maneuvering. But Mercedes is larger and more comfortable on longer trips."
41 OK: Mercedes GLE > BMW X5 — keep as-is
41 RECODE: Mercedes GLE > BMW X5 — weight_base 1.5 → 3.0
42 OK: Mercedes GLE > BMW X5 — keep as-is
43 OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I was pretty torn between the 2 and ended up buying the X5. The merc seemed quieter and smoother to drive but also lacked anything that I would consider fun. I was in the 4 cylinder 350 though. … The bmw just felt much more connected to the road…"
44 OK: BMW X5 > Mercedes GLE — keep as-is
45 DELETE: BMW X5 > Mercedes GLE — remove row
46 OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I have had both and currently have the X5. … I do miss the merc seats but the BMW are nice too. Felt the Benz seats were buttery and plush. Space in the rear - Benz is bigger for 2nd row and cargo."
47 RECODE: BMW X5 > Mercedes GLE — evidence test_drove_both → owned_one_td_other
48 OK: BMW X5 > Mercedes GLE — keep as-is; fuller quote suggested: "I'm not a BMW guy. This X5 is my first one. I test drove all the foreign luxury mid size SUVs with an open mind. … That said, with the inexpensive Multi contour seats option, the X5 seats are more comfortable and adjustable than anything else I tried, including the highest end Cayenne seats. The Merc seats are ok, but nothing special in the segment."
49 OK: BMW X5 > Porsche Cayenne — keep as-is; fuller quote suggested: "I'm not a BMW guy. This X5 is my first one. I test drove all the foreign luxury mid size SUVs with an open mind. … That said, with the inexpensive Multi contour seats option, the X5 seats are more comfortable and adjustable than anything else I tried, including the highest end Cayenne seats. The Merc seats are ok, but nothing special in the segment."
50 RECODE: BMW X5 > Mercedes GLE — evidence test_drove_both → owned_both
51 RECODE: Volvo XC90 > Land Rover Defender — evidence owned_both → opinion
52 OK: Volvo XC90 > Land Rover Defender — keep as-is; fuller quote suggested: "I traded in my 2023 XC90 when the lease ended for a 2025 Land Rover Defender 110. Two different vehicles for sure, but I miss the subtlety of the Volvo and the ergonomics of that car. It was so comfortable to drive!"
53 OK: Volvo XC90 > Rivian R1S — keep as-is
54 OK: BMW X5 > Volvo XC90 — keep as-is; fuller quote suggested: "I test drove the XC90, Lincoln Aviator, and BMW X5. I chose the X5. … The air suspension was great but still felt bulky. The X5 was an amazing blend of comfort and sporty handling, and I fell in love with it."
55 RECODE: Volvo XC90 > BMW X5 — evidence owned_both → test_drove_both
55 RECODE: Volvo XC90 > BMW X5 — weight 1.5 → 2.0
56 OK: BMW X7 > Volvo XC90 — keep as-is; fuller quote suggested: "I moved on to an X7 M50i and EQS SUV after having an XC90 for 7yrs. … The biggest issue I had with the car … is the lack of noise insulation. … it just felt noisy inside. … When I got my X7, it was worlds better where I felt like I could have a quiet conversation in the car even when the v8 is cranking and the EQS took it another step up in serene-ness."
57 OK: Mercedes EQS SUV > Volvo XC90 — keep as-is; fuller quote suggested: "I moved on to an X7 M50i and EQS SUV after having an XC90 for 7yrs. … The biggest issue I had with the car … is the lack of noise insulation. … it just felt noisy inside. … When I got my X7, it was worlds better where I felt like I could have a quiet conversation in the car even when the v8 is cranking and the EQS took it another step up in serene-ness."
58 OK: Volvo XC90 > BMW X7 — keep as-is
59 QUOTE_FIX: Volvo XC90 > Mercedes GLE — replace quote with: "but I've had a '24 GLE350 as a service loaner a couple of times and while that does feel a bit more solid and the interior is nicer, I still prefer the XC90."
59 RECODE: Volvo XC90 > Mercedes GLE — axis seats → overall
60 RECODE: Volvo XC90 > Mercedes GLE — evidence test_drove_both → owned_one_td_other [model not named — thread inference]
61 QUOTE_FIX: BMW X5 > Volvo XC90 — replace quote with: "I just came from BMW, which was better in every way. But hopefully the Volvo is more reliable which is what I need right now. …It was more comfy and the ride was nicer on longer drives? … Yes. Bigger engine with a smoother ride."
62 DELETE: Volvo XC90 > Audi Q7 — remove row
63 OK: Volvo XC90 > Subaru Forester — keep as-is
64 OK: Lexus RX > Hyundai Palisade — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
65 OK: Lexus RX > Genesis GV80 — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
66 OK: Lexus RX > Honda Passport — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
67 RECODE: Cadillac Escalade > Lexus LX — evidence owned_one_td_other → opinion
67 RECODE: Cadillac Escalade > Lexus LX — home_team 1 → 0
68 RECODE: Audi Q8 > Lexus NX — evidence test_drove_both → opinion
69 RECODE: Range Rover > Lexus RX — evidence owned_one_td_other → opinion_plus_drive [model not named — thread inference]
70 DELETE: Range Rover > Mercedes GLE — remove row
71 DELETE: Range Rover > BMW X5 — remove row
72 RECODE: Lexus ES > Lexus RX — evidence owned_both → test_drove_both
73 RECODE: Genesis GV80 > Lincoln Navigator — evidence test_drove_both → opinion
74 QUOTE_FIX: Lincoln Navigator > Hyundai Palisade — replace quote with: "…My wife loves her '23 Palisade and she has owned a laundry list of luxury/premium brand SUV's before it. I've been surprised with it as well in terms of ride and comfort, particularly for the cost, but I wouldn't put it anywhere near the top of the charts. I have an Escalade in the biz fleet that's very comfortable all around but I think the newest Navigator is probably better."
74 RECODE: Lincoln Navigator > Hyundai Palisade — evidence owned_one_td_other → opinion_plus_drive
75 QUOTE_FIX: Cadillac Escalade > Hyundai Palisade — replace quote with: "…My wife loves her '23 Palisade and she has owned a laundry list of luxury/premium brand SUV's before it. I've been surprised with it as well in terms of ride and comfort, particularly for the cost, but I wouldn't put it anywhere near the top of the charts. I have an Escalade in the biz fleet that's very comfortable all around but I think the newest Navigator is probably better."
76 DELETE: Range Rover > Hyundai Palisade — remove row
77 OK: Lexus LX > Genesis GV80 — keep as-is; fuller quote suggested: "I replaced my 2013 Lexus at 300K miles with a new LX after driving everything else in the price range. I will say the Genesis GV was close 2nd overall in my comparisons in comfort/driver features/ride/cabin noise, but was a bit too small… Mercedes GLS was my size equivalent 2nd choice and matches the Lexus pretty well. But the Lexus with the adaptive suspension is just a very pleasant car to own."
78 OK: Lexus LX > Mercedes GLS — keep as-is; fuller quote suggested: "I replaced my 2013 Lexus at 300K miles with a new LX after driving everything else in the price range. I will say the Genesis GV was close 2nd overall in my comparisons in comfort/driver features/ride/cabin noise, but was a bit too small… Mercedes GLS was my size equivalent 2nd choice and matches the Lexus pretty well. But the Lexus with the adaptive suspension is just a very pleasant car to own."
79 OK: Range Rover > Range Rover Sport — keep as-is
80 QUOTE_FIX: Range Rover Sport > Mercedes GLE — replace quote with: "…of all the vehicles my wife and I have owned… the GLE was perhaps the poorest handling of them all… I hated how it drove. … What's nice is that I never felt tired after a long trip from Vegas to L.A. and back."
81 OK: Range Rover Sport > Porsche Cayenne — keep as-is
82 QUOTE_FIX: Range Rover Sport > BMW X5 — replace quote with: "I test drove a Cayenne, X5 and a RRS. Porsche felt sporty, Range Rover felt like sitting on a cloud and more luxury. … I chose my RRS."
83 OK: Range Rover Sport > Porsche Cayenne — keep as-is
84 RECODE: Range Rover Sport > Mercedes GLE — evidence test_drove_both → opinion_plus_drive
85 OK: Range Rover > Audi Q8 — keep as-is
86 OK: Range Rover Sport > Volvo XC90 — keep as-is; fuller quote suggested: "Before we briefly had an XC90 T8 Recharge. I didn't really like the Volvo that much: It was quite 'boaty' (swaying left and right in turns and up and down when accelerating and breaking)… the Range Rover in my opinion looks better and the driving feel is almost incomparable."
87 OK: Tesla Model X > Tesla Model Y — keep as-is
88 RECODE: Hyundai Palisade > Tesla Model Y — evidence owned_one_td_other → opinion
89 OK: Hyundai Palisade > Kia Telluride — keep as-is
89 RECODE: Hyundai Palisade > Kia Telluride — home_team 0 → 1
90 RECODE: Hyundai Palisade > Kia Telluride — evidence test_drove_both → owned_one_td_other
90 RECODE: Hyundai Palisade > Kia Telluride — home_team 0 → 1
91 OK: Kia Telluride > Hyundai Palisade — keep as-is
92 RECODE: Land Rover > Volvo XC60 — evidence test_drove_both → opinion_plus_drive
92 QUOTE_FIX: Land Rover > Volvo XC60 — replace quote with: "When I test drove the XC60 i think it either had 20" wheels or run flats because it rode like shit. … For comfort the only answer is a Land Rover product (includes Range Rover). You have to sacrifice on reliability but they have air suspension / cushy seats figured out."
93 OK: Volvo XC60 > BMW X1 — keep as-is
94 RECODE: Audi Q5 > BMW X3 — evidence owned_one_td_other → opinion
95 QUOTE_FIX: Volvo XC60 > BMW X3 — replace quote with: "Volvo is great, with a bit of a soft ride. BMW x3 is more on the firm side."
95 RECODE: Volvo XC60 > BMW X3 — evidence owned_one_td_other → opinion
96 DELETE: Toyota Highlander > Honda CR-V — remove row
97 DELETE: Mazda CX-9 > Mazda CX-50 — remove row
98 DELETE: Acura MDX > Lexus RX — remove row
99 OK: Genesis GV80 > Mercedes GLE — keep as-is
100 OK: Genesis GV80 > BMW X5 — keep as-is
101 OK: BMW X5 > Mercedes GLE — keep as-is; fuller quote suggested: "GLE feels heavier, like driving a pontoon boat. The X5 feels like a ski boat. Light, nimble, like its gliding along the road… Overall I enjoy the X5 so much better than the MB, mainly because of the ride and smooth acceleration."
102 OK: Range Rover Sport > Mercedes GLE AMG — keep as-is
102 RECODE: Range Rover Sport > Mercedes GLE AMG — home_team 0 → 1
103 QUOTE_FIX: BMW iX > Tesla Model X — replace quote with: "The new BMW iX handles better than the Tesla Model X. The new BMW iX is more refined than the Model X. The new BMW iX is more comfortable than the Model X."
104 OK: Hyundai Palisade > Mazda CX-90 — keep as-is
105 RECODE: Hyundai Palisade > Toyota Grand Highlander — evidence test_drove_both → opinion_plus_drive
106 RECODE: Lexus TX > Toyota Grand Highlander — evidence test_drove_both → opinion
107 OK: Hyundai Palisade > Toyota Highlander — keep as-is
108 OK: Toyota Highlander > Hyundai Palisade — keep as-is
109 OK: Toyota Highlander > Honda Pilot — keep as-is [model not named — thread inference]
110 OK: Toyota Grand Highlander > Hyundai Palisade — keep as-is
111 OK: Hyundai Palisade > Toyota Grand Highlander — keep as-is
112 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → opinion
113 OK: Hyundai Palisade > Honda Pilot — keep as-is
114 RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → opinion_plus_drive
114 QUOTE_FIX: Hyundai Palisade > Honda Pilot — add parent/thread context: "Palisade vs Pilot"
115 RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → opinion_plus_drive
115 QUOTE_FIX: Hyundai Palisade > Honda Pilot — add parent/thread context: "Palisade vs Pilot"
116 OK: Hyundai Palisade > Kia Telluride — keep as-is
117 OK: Hyundai Palisade > Toyota Highlander — keep as-is
118 OK: Hyundai Palisade > Kia Telluride — keep as-is
119 DELETE: Hyundai Palisade > Lexus TX — remove row
120 DELETE: Hyundai Palisade > Toyota Grand Highlander — remove row
121 OK: Hyundai Palisade > Toyota Highlander — keep as-is
122 OK: Lincoln Aviator > BMW X5 — keep as-is
123 QUOTE_FIX: Lincoln Aviator > BMW X5 — replace quote with: "I have a 2025 X5 and a 2026 Aviator..... My personal favorite of the 2 is the Aviator but I love the X5 as well. Both feel very premium… the Aviator is smoother. The BMW is quicker but the Aviator is more powerful…"
124 OK: BMW X5 > Lincoln Aviator — keep as-is
125 OK: BMW X7 > Lincoln Aviator — keep as-is
126 OK: Lincoln Aviator > BMW X7 — keep as-is
126 RECODE: Lincoln Aviator > BMW X7 — home_team 0 → 1
127 OK: Lincoln Aviator > Lexus TX — keep as-is
127 RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
128 OK: Mercedes GLS > BMW X7 — keep as-is
129 OK: Mercedes GLS > BMW X7 — keep as-is
130 OK: Mercedes GLS > BMW X7 — keep as-is
131 OK: Mercedes GLS > BMW X7 — keep as-is
132 RECODE: Cadillac Escalade > BMW X7 — evidence opinion_plus_drive → opinion
133 OK: BMW X7 > Cadillac Escalade — keep as-is
133 QUOTE_FIX: BMW X7 > Cadillac Escalade — replace quote with: "…the kids are actually a bit more comfortable in the second row than the Caddy… I find it to ride smoother than the Caddy."
134 OK: Tesla Model X > Cadillac Escalade — keep as-is
134 RECODE: Tesla Model X > Cadillac Escalade — home_team 0 → 1
135 OK: Cadillac Escalade > Tesla Model X — keep as-is
136 OK: Cadillac Escalade > Tesla Model X — keep as-is
137 OK: Lincoln Nautilus > Lexus RX — keep as-is [model not named — thread inference]
138 OK: Volvo XC60 > Lincoln Nautilus — keep as-is [model not named — thread inference]
138 RECODE: Volvo XC60 > Lincoln Nautilus — home_team 0 → 1
139 OK: Lincoln Nautilus > Volvo XC60 — keep as-is [model not named — thread inference]
140 RECODE: Audi Q7 > Volvo XC90 — evidence test_drove_both → opinion
141 RECODE: Volvo XC90 > Audi Q7 — evidence test_drove_both → opinion
142 OK: Audi Q7 > Volvo XC90 — keep as-is
143 OK: Audi Q7 > Volvo XC90 — keep as-is
143 RECODE: Audi Q7 > Volvo XC90 — home_team 0 → 1
144 OK: Hyundai Palisade > Lincoln Nautilus — keep as-is
145 OK: Hyundai Palisade > Lincoln Aviator — keep as-is
146 OK: Hyundai Palisade > Ford Explorer — keep as-is
147 OK: Hyundai Palisade > Honda Pilot — keep as-is
148 OK: Ford Explorer > Kia Telluride — keep as-is
149 OK: Kia Telluride > Honda Pilot — keep as-is
150 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
151 OK: Cadillac Escalade > Lincoln Navigator — keep as-is
152 DELETE: Mercedes GLS > Lincoln Navigator — remove row
153 OK: Toyota Highlander > Toyota RAV4 — keep as-is
154 OK: Honda CR-V > Toyota RAV4 — keep as-is
155 QUOTE_FIX: Hyundai Palisade > Toyota Highlander — replace quote with: "I owned a 2020 palisade platinum and a 2023 highlighter platinum. The Palisade ride is alot smoother"
156 OK: Hyundai Palisade > Honda Pilot — keep as-is
157 RECODE: Honda Pilot > Hyundai Palisade — evidence test_drove_both → opinion_plus_drive
157 RECODE: Honda Pilot > Hyundai Palisade — home_team 0 → 1
158 OK: Hyundai Palisade > Toyota Highlander — keep as-is [model not named — thread inference]
158 RECODE: Hyundai Palisade > Toyota Highlander — home_team 0 → 1
159 OK: Hyundai Palisade > Honda Pilot — keep as-is [model not named — thread inference]
159 RECODE: Hyundai Palisade > Honda Pilot — home_team 0 → 1
160 RECODE: Hyundai Palisade > Volkswagen Atlas — evidence test_drove_both → opinion_plus_drive
160 RECODE: Hyundai Palisade > Volkswagen Atlas — home_team 0 → 1
161 OK: Hyundai Palisade > Honda Pilot — keep as-is
161 RECODE: Hyundai Palisade > Honda Pilot — home_team 0 → 1
162 OK: Hyundai Palisade > Kia Telluride — keep as-is
163 OK: Hyundai Palisade > Toyota Highlander — keep as-is
164 DELETE: Hyundai Palisade > Toyota Grand Highlander — remove row
165 OK: Hyundai Palisade > Mazda CX-90 — keep as-is [model not named — thread inference]
165 RECODE: Hyundai Palisade > Mazda CX-90 — home_team 0 → 1
166 RECODE: Mazda CX-90 > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
166 RECODE: Mazda CX-90 > Hyundai Palisade — home_team 0 → 1
167 OK: Hyundai Palisade > Toyota Grand Highlander — keep as-is [model not named — thread inference]
167 RECODE: Hyundai Palisade > Toyota Grand Highlander — home_team 0 → 1
168 RECODE: Toyota Grand Highlander > Hyundai Palisade — evidence test_drove_both → opinion
169 OK: Hyundai Palisade > Subaru Ascent — keep as-is
169 RECODE: Hyundai Palisade > Subaru Ascent — home_team 0 → 1
170 OK: Subaru Ascent > Hyundai Palisade — keep as-is [model not named — thread inference]
170 RECODE: Subaru Ascent > Hyundai Palisade — home_team 0 → 1
171 OK: Hyundai Palisade > Toyota Highlander — keep as-is
172 OK: Hyundai Palisade > Honda Pilot — keep as-is
173 OK: Subaru Ascent > Hyundai Palisade — keep as-is [model not named — thread inference]
174 OK: Subaru Ascent > Kia Telluride — keep as-is [model not named — thread inference]
175 OK: Subaru Ascent > Toyota Grand Highlander — keep as-is [model not named — thread inference]
176 OK: Kia Telluride > Ford Explorer — keep as-is
176 RECODE: Kia Telluride > Ford Explorer — home_team 0 → 1
177 OK: Kia Telluride > Toyota Highlander — keep as-is
177 RECODE: Kia Telluride > Toyota Highlander — home_team 0 → 1
178 OK: Honda Pilot > Toyota Highlander — keep as-is
178 RECODE: Honda Pilot > Toyota Highlander — home_team 0 → 1
179 OK: Toyota Grand Highlander > Hyundai Palisade — keep as-is
179 RECODE: Toyota Grand Highlander > Hyundai Palisade — home_team 0 → 1
180 OK: Toyota Grand Highlander > Kia Telluride — keep as-is
180 RECODE: Toyota Grand Highlander > Kia Telluride — home_team 0 → 1
181 OK: Lincoln Aviator > Volvo XC90 — keep as-is
182 OK: Lincoln Aviator > BMW X5 — keep as-is
183 OK: Cadillac Escalade > Lincoln Navigator — keep as-is
184 OK: Cadillac Escalade > Lincoln Navigator — keep as-is [model not named — thread inference]
184 RECODE: Cadillac Escalade > Lincoln Navigator — home_team 1 → 0
185 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
186 OK: Cadillac Escalade > Lincoln Navigator — keep as-is [model not named — thread inference]
187 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
188 OK: Audi Q7 > BMW X5 — keep as-is
189 OK: Audi Q7 > BMW X5 — keep as-is
190 OK: Audi Q8 > Audi Q7 — keep as-is
191 QUOTE_FIX: BMW X5 > Acura MDX — replace quote with: "For the suspension, I'd say it was like the MDX but more refined. It handled imperfections much better"
192 OK: Acura MDX > Audi Q7 — keep as-is
193 RECODE: Acura MDX > BMW X5 — evidence owned_both → test_drove_both [model not named — thread inference]
194 OK: BMW X5 > Lexus GX — keep as-is
195 OK: BMW X7 > Lexus GX — keep as-is
196 OK: Lincoln Nautilus > Lexus RX — keep as-is
197 OK: Genesis GV80 > BMW X5 — keep as-is
198 QUOTE_FIX: Genesis GV70 > Audi Q5 — replace quote with: "GV70 was most comfortable by a decent margin with the Volvo in second"
199 OK: Porsche Cayenne > BMW X5 — keep as-is
200 OK: Mercedes GLC > BMW X3 — keep as-is
201 QUOTE_FIX: Mercedes GLC > BMW X3 — replace quote with: "the Mercedes was FAR more comfortable for us… you get more comfort snd quiet with Mercedes"
201 RECODE: Mercedes GLC > BMW X3 — evidence test_drove_both → owned_one_td_other
202 QUOTE_FIX: Acura MDX > Volvo XC90 — replace quote with: "I own a 2016 xc90… and 2022 MDX tech… MDX smoother ride, absorbs bumps better, feels larger than xc90…"
203 OK: Lexus RX > BMW X5 — keep as-is
204 OK: Genesis GV70 > Volvo XC60 — keep as-is
205 OK: Lexus RX > Volvo XC60 — keep as-is
206 RECODE: Honda Pilot > Kia Telluride — evidence test_drove_both → owned_one_td_other
207 UNVERIFIED: Toyota Highlander > Toyota Venza — page unreachable; keep as-is; re-audit when fetchable; quote contains coder-editorial bracket
208 OK: Toyota Venza > Toyota Highlander — keep as-is
209 UNVERIFIED: Hyundai Palisade > Honda CR-V — page unreachable; keep as-is; re-audit when fetchable
210 UNVERIFIED: Hyundai Palisade > Kia Telluride — page unreachable; keep as-is; re-audit when fetchable
211 OK: Subaru Outback > Honda CR-V — keep as-is
212 UNVERIFIED: Mazda CX-5 > Toyota RAV4 — page unreachable; keep as-is; re-audit when fetchable
213 UNVERIFIED: Honda CR-V > Mazda CX-50 — page unreachable; keep as-is; re-audit when fetchable
214 UNVERIFIED: Mazda CX-5 > Mazda CX-50 — page unreachable; keep as-is; re-audit when fetchable
215 UNVERIFIED: Mazda CX-50 > Mazda CX-5 — page unreachable; keep as-is; re-audit when fetchable
216 OK: Honda Pilot > Honda CR-V — keep as-is
217 OK: Lincoln Aviator > Lexus RX — keep as-is
218 OK: Lexus NX > Lexus RX — keep as-is
219 OK: Subaru Outback > Toyota RAV4 — keep as-is
222 RECODE: Subaru Outback > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
224 OK: Subaru Outback > Subaru Forester — keep as-is
224 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
228 OK: Subaru Outback > Subaru Crosstrek — keep as-is
228 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
229 OK: Honda CR-V > Subaru Outback — keep as-is
230 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
232 QUOTE_FIX: Subaru Outback 2026 > Subaru Forester — replace quote with: "To be fair, it is nicer in a lot of ways — quieter cabin, smoother ride… but I couldn't get past the driving position and sightlines"
232 RECODE: Subaru Outback 2026 > Subaru Forester — evidence test_drove_both → owned_one_td_other
233 OK: Subaru Outback 2026 > Toyota 4Runner — keep as-is [model not named — thread inference]
234 OK: Subaru Ascent > Hyundai Palisade — keep as-is
235 OK: Subaru Ascent > Kia Telluride — keep as-is
236 OK: Subaru Ascent > Toyota Highlander — keep as-is
237 OK: Kia Telluride > Subaru Ascent — keep as-is
238 RECODE: Subaru Ascent > Kia Telluride — evidence test_drove_both → owned_one_td_other
239 RECODE: Subaru Ascent > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
240 RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
242 QUOTE_FIX: Subaru Ascent > Subaru Outback — replace quote with: "We test drove all 3 and at 70mph the Ascent was roughly 5dB quieter than both. Suspension is softest, more comfortable on bad Michigan roads"
242 RECODE: Subaru Ascent > Subaru Outback — evidence test_drove_both → owned_one_td_other
243 QUOTE_FIX: Subaru Ascent > Subaru Forester — replace quote with: "We test drove all 3 and at 70mph the Ascent was roughly 5dB quieter than both"
243 RECODE: Subaru Ascent > Subaru Forester — evidence test_drove_both → owned_one_td_other
246 OK: Subaru Ascent > Chevrolet Suburban — keep as-is [model not named — thread inference]
247 OK: Lexus RX > Lexus GX — keep as-is
247 RECODE: Lexus RX > Lexus GX — home_team 0 → 1
249 QUOTE_FIX: Lexus GX > Lexus RX — replace quote with: "I had the 2021 RX 350 and now the 2023 GX 460… I enjoy the ride of the GX 460 better. I think that the ride is smoother"
249 RECODE: Lexus GX > Lexus RX — home_team 0 → 1
253 OK: Lexus RX > Toyota Highlander — keep as-is
253 RECODE: Lexus RX > Toyota Highlander — home_team 0 → 1
255 RECODE: Lexus GX > Toyota 4Runner — evidence test_drove_both → owned_one_td_other [model not named — thread inference]
259 OK: Lexus GX > Toyota 4Runner — keep as-is
261 OK: Lexus GX > Toyota 4Runner — keep as-is
262 OK: Subaru Outback > Toyota RAV4 — keep as-is
263 OK: Subaru Outback > Toyota RAV4 — keep as-is
264 OK: Subaru Outback > Toyota RAV4 — keep as-is
265 RECODE: Subaru Outback > Subaru Forester — evidence owned_both → opinion_plus_drive
265 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
266 OK: Subaru Outback > Subaru Forester — keep as-is
266 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
267 OK: Subaru Outback > Subaru Forester — keep as-is
267 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
268 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
269 RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
270 OK: Subaru Ascent > Subaru Outback — keep as-is
271 OK: Subaru Ascent > Subaru Forester — keep as-is
272 OK: Lexus RX > Lexus GX — keep as-is
272 RECODE: Lexus RX > Lexus GX — home_team 0 → 1
273 OK: Lexus GX > Lexus RX — keep as-is
273 RECODE: Lexus GX > Lexus RX — home_team 0 → 1
274 QUOTE_FIX: Lexus GX > Lexus RX — replace quote with: "I own a GX… driven an RX loaner… less wind/road noise"
274 RECODE: Lexus GX > Lexus RX — home_team 0 → 1
275 OK: Lexus RX > Lexus GX — keep as-is
275 RECODE: Lexus RX > Lexus GX — home_team 0 → 1
276 QUOTE_FIX: Lexus RX > Toyota Highlander — replace quote with: "We made the trade… it is such a smoother ride. Quieter cabin, smooth V6, so comfortable"
276 RECODE: Lexus RX > Toyota Highlander — home_team 0 → 1
277 OK: Lexus GX > Toyota 4Runner — keep as-is
278 OK: Lexus GX > Toyota 4Runner — keep as-is
279 OK: Lexus GX > Toyota 4Runner — keep as-is
280 OK: Lexus GX > Toyota 4Runner — keep as-is
281 OK: Subaru Outback > Honda CR-V — keep as-is
282 OK: Subaru Outback > Honda CR-V — keep as-is [model not named — thread inference]
283 QUOTE_FIX: Subaru Outback > Honda CR-V — replace quote with: "I have both. A 2024 crv sport touring (hybrid) and a 2025 outback touring XT… for me the outback wins in comfort - both as driver and passenger… after driving the Outback for a few months, it now seems noisier to me"
284 OK: Honda CR-V > Subaru Outback — keep as-is
284 RECODE: Honda CR-V > Subaru Outback — home_team 1 → 0
285 OK: Subaru Outback > Honda CR-V — keep as-is
286 OK: Honda CR-V > Subaru Outback — keep as-is
287 OK: Honda CR-V > Subaru Outback — keep as-is
288 QUOTE_FIX: Mazda CX-5 > Subaru Outback — replace quote with: "Test of very low miles CX-5… Very quiet. Little road noise… 2024 Outback demo… Suspension was just harsh… Lots of road noise, lots of suspension noise"
289 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
290 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
291 OK: Honda CR-V > Subaru Outback 2026 — keep as-is
291 RECODE: Honda CR-V > Subaru Outback 2026 — home_team 1 → 0
292 QUOTE_FIX: Subaru Outback 2026 > Honda CR-V — replace quote with: "The driver seat was okay… not as lounge comforting as the OB… Sitting drivers in the OB was just very comfortable"
293 OK: Subaru Outback 2026 > Subaru Ascent — keep as-is [model not named — thread inference]
294 OK: Subaru Outback 2026 > Toyota RAV4 — keep as-is [model not named — thread inference]
295 OK: Hyundai Palisade > Subaru Ascent — keep as-is
296 OK: Subaru Ascent > Hyundai Palisade — keep as-is
297 OK: Honda Pilot > Subaru Ascent — keep as-is
298 OK: Honda Pilot > Subaru Ascent — keep as-is
299 OK: Subaru Outback > Subaru Ascent — keep as-is
300 OK: Subaru Outback > Subaru Ascent — keep as-is
301 OK: Subaru Ascent > Subaru Outback — keep as-is
302 OK: Subaru Ascent > Subaru Outback — keep as-is
303 RECODE: Subaru Ascent > Volkswagen Atlas — evidence test_drove_both → owned_one_td_other
304 RECODE: Subaru Ascent > Toyota Highlander — evidence test_drove_both → owned_one_td_other
305 RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
306 OK: Hyundai Palisade > Subaru Ascent — keep as-is [model not named — thread inference]
307 OK: Lexus RX > Toyota RAV4 — keep as-is
308 QUOTE_FIX: Lexus RX > Audi Q5 — replace quote with: "I traded my 2016 Audi Q5 Premium Plus for the RX350 Premium AWD… Very comfortable and roomy… Seating in the Audi Q5 was very tight"
309 QUOTE_FIX: Volvo XC90 > Lexus RX — replace quote with: "I was so disappointed with the RX. Test drove against the cx-9, MDX, xc90, gle350, q7, and x5. Easily the most jarring ride"
310 OK: Lexus RX > Lexus GX — keep as-is
310 RECODE: Lexus RX > Lexus GX — home_team 0 → 1
311 QUOTE_FIX: Lexus RX > Lexus GX — replace quote with: "I moved from RX to GX. Ride is definitely day and night difference. You'll probably notice that coming from BMW X5. But again GX is a truck body on frame."
312 OK: Lexus GX > Lexus RX — keep as-is
313 OK: Lexus GX > Lexus TX — keep as-is
314 OK: Lexus TX > Lexus GX — keep as-is
314 RECODE: Lexus TX > Lexus GX — home_team 0 → 1
315 OK: Lexus LX > Lexus GX — keep as-is
316 OK: Lexus LX > Lexus GX — keep as-is [model not named — thread inference]
317 OK: Lexus GX > Toyota 4Runner — keep as-is
318 RECODE: Lexus GX > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
319 OK: Lexus GX > Lexus GX 550 — keep as-is [model not named — thread inference]
320 QUOTE_FIX: Lexus RX > Audi Q7 — replace quote with: "Ride quality is meh compared to RX350L or at least imo. Even the 55"
320 RECODE: Lexus RX > Audi Q7 — evidence test_drove_both → opinion
321 OK: Lexus NX > Mercedes GLC — keep as-is
322 OK: Lexus NX > Mercedes GLC — keep as-is
323 OK: Lincoln Corsair > BMW X3 — keep as-is
324 OK: Lincoln Nautilus > BMW X3 — keep as-is
325 OK: GV70 > Macan — keep as-is
326 OK: GV70 > Q5 — keep as-is
327 OK: GV70 > BMW X3 — keep as-is
328 OK: Macan > BMW X3 — keep as-is
329 OK: Q5 > BMW X3 — keep as-is
330 OK: GV70 > Porsche Macan — keep as-is
331 OK: GV70 > Audi Q5 — keep as-is
332 OK: Lincoln Nautilus > Lexus RX — keep as-is
333 OK: Toyota Venza > Honda CR-V — keep as-is
334 QUOTE_FIX: Toyota Venza > Honda CR-V — replace quote with: "My Venza is like a baby Lexus on the inside. The seat comfort is PHENOMENAL and the main reason I bought the car. I have to haul a lot of equipment and move large boxes with my job, so I miss the cargo practicality of my CR-V."
335 RECODE: Honda CR-V > Toyota Venza — evidence test_drove_both → owned_one_td_other
336 OK: Volvo XC60 > Lexus NX — keep as-is
337 RECODE: Volvo XC60 > Lexus NX — evidence test_drove_both → owned_one_td_other
338 OK: Volvo XC60 > Lexus NX — keep as-is
339 RECODE: Lexus NX > Volvo XC60 — evidence test_drove_both → owned_one_td_other
340 OK: Volvo XC60 > Porsche Macan — keep as-is [model not named — thread inference]
341 OK: Honda CR-V > Mazda CX-50 — keep as-is
342 OK: Mazda CX-5 > Mazda CX-50 — keep as-is
343 OK: Honda CR-V > Mazda CX-50 — keep as-is
344 RECODE: Honda CR-V > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
345 RECODE: Honda CR-V > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
346 OK: Honda CR-V > Mazda CX-50 — keep as-is
347 RECODE: Honda CR-V > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
348 OK: Honda CR-V > Mazda CX-5 — keep as-is [model not named — thread inference]
349 OK: Volvo XC60 > Audi Q5 — keep as-is
350 OK: Audi Q5 > Mercedes GLC — keep as-is
351 RECODE: Lincoln Nautilus > Cadillac XT5 — evidence test_drove_both → owned_one_td_other
352 OK: Lincoln Nautilus > Cadillac XT5 — keep as-is
353 OK: Honda CR-V > Volkswagen Tiguan — keep as-is
354 RECODE: Honda CR-V > Volkswagen Tiguan — evidence test_drove_both → owned_one_td_other
355 OK: Audi Q5 > Lexus NX — keep as-is
356 OK: Genesis GV70 > BMW X3 — keep as-is [model not named — thread inference]
357 RECODE: Genesis GV70 > BMW X3 — evidence test_drove_both → owned_one_td_other
358 OK: Mercedes GLE > Volvo XC90 — keep as-is [model not named — thread inference]
359 OK: Mercedes GLE > Audi Q7 — keep as-is [model not named — thread inference]
360 RECODE: Audi Q7 > BMW X5 — evidence test_drove_both → owned_one_td_other
361 RECODE: Audi Q7 > Mercedes GLE — evidence test_drove_both → owned_one_td_other
362 RECODE: Lincoln Aviator > Genesis GV80 — evidence test_drove_both → owned_one_td_other
363 RECODE: Lincoln Aviator > Genesis GV80 — evidence test_drove_both → owned_one_td_other
364 RECODE: Acura MDX > Genesis GV80 — evidence test_drove_both → owned_one_td_other
365 OK: Mercedes GLE > Porsche Cayenne — keep as-is
366 OK: BMW X5 > Tesla Model X — keep as-is
367 OK: BMW iX > Tesla Model X — keep as-is
368 OK: BMW iX > Tesla Model X — keep as-is
369 QUOTE_FIX: BMW iX > Tesla Model X — replace quote with: "DRIVE QUALITY/ROAD NOISE —> all caps because it's not remotely close; you can barely have a conversation on the highway in the X"
370 OK: BMW iX > Tesla Model X — keep as-is
371 OK: Acura MDX > BMW X5 — keep as-is
372 OK: Acura MDX > BMW X5 — keep as-is
373 OK: BMW X5 > Acura MDX — keep as-is
374 RECODE: Lexus TX > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
375 OK: Lincoln Aviator > Volvo XC90 — keep as-is
376 RECODE: BMW iX > Mercedes EQS SUV — evidence test_drove_both → owned_one_td_other
377 OK: BMW iX > BMW X5 — keep as-is
378 OK: BMW iX > BMW X5 — keep as-is
379 RECODE: BMW iX > BMW X5 — evidence owned_one_loaner → owned_both
380 RECODE: BMW X5 > BMW iX — evidence test_drove_both → owned_one_td_other
381 OK: BMW X5 > Tesla Model Y — keep as-is
382 OK: BMW X5 > Tesla Model Y — keep as-is
383 OK: Audi Q8 > Genesis GV80 — keep as-is
384 OK: Acura MDX > Genesis GV80 — keep as-is
385 OK: Kia Telluride > Nissan Pathfinder — keep as-is
386 OK: Nissan Pathfinder > Honda Pilot — keep as-is
387 RECODE: Nissan Pathfinder > Honda Passport — evidence test_drove_both → owned_one_td_other
388 RECODE: Nissan Pathfinder > Honda Pilot — evidence test_drove_both → owned_one_td_other
389 OK: Nissan Pathfinder > Honda Pilot — keep as-is
390 OK: Nissan Pathfinder > Honda Pilot — keep as-is
391 OK: Nissan Pathfinder > Honda Pilot — keep as-is
392 RECODE: Nissan Pathfinder > Honda Pilot — evidence test_drove_both → owned_one_td_other
393 OK: Kia Telluride > Kia Sorento — keep as-is
394 OK: Kia Telluride > Kia Sorento — keep as-is [model not named — thread inference]
395 RECODE: Kia Telluride > Kia Sorento — evidence test_drove_both → owned_one_td_other
396 OK: Honda Passport > Honda Pilot — keep as-is
397 RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
398 RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
399 RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
400 OK: Volkswagen Atlas > Honda Pilot — keep as-is
401 OK: Honda Pilot > Kia Telluride — keep as-is
402 OK: Kia Telluride > Honda Pilot — keep as-is
403 OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
404 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
405 RECODE: Kia Telluride > Volkswagen Atlas — evidence owned_one_td_other → test_drove_both
406 OK: Volkswagen Atlas > Kia Telluride — keep as-is
407 OK: Hyundai Palisade > Nissan Pathfinder — keep as-is
408 RECODE: Hyundai Palisade > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
409 OK: Hyundai Palisade > Nissan Pathfinder — keep as-is
410 RECODE: Hyundai Palisade > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
411 OK: Kia Telluride > Ford Explorer — keep as-is [model not named — thread inference]
412 QUOTE_FIX: Kia Telluride > Ford Explorer — replace quote with: "I had a 2017 Explorer, and it drove bulky like a truck… It handles like a car"
413 OK: Kia Telluride > Ford Explorer — keep as-is
414 OK: Honda Pilot > Honda Passport — keep as-is
415 OK: Honda Pilot > Honda Passport — keep as-is
416 RECODE: Honda Pilot > Honda Passport — evidence test_drove_both → owned_one_td_other
417 QUOTE_FIX: Honda Passport > Honda Pilot — replace quote with: "the seats are very uncomfortable… I loved the comfort of the seat"
417 RECODE: Honda Passport > Honda Pilot — evidence test_drove_both → owned_one_td_other
418 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
419 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
420 QUOTE_FIX: Honda Pilot > Toyota Grand Highlander — replace quote with: "We thought the GH was like driving a boat and I've seen some say they've gotten carsick either driving or riding in the GH."
420 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
421 OK: Honda Pilot > Volkswagen Atlas — keep as-is
422 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
423 RECODE: Honda Pilot > Toyota Highlander — evidence test_drove_both → owned_one_td_other
424 RECODE: Honda Pilot > Kia Telluride — evidence test_drove_both → owned_one_td_other
425 OK: Nissan Pathfinder > Honda Pilot — keep as-is
426 OK: Nissan Pathfinder > Toyota Highlander — keep as-is
427 QUOTE_FIX: Kia Telluride > Honda Pilot — replace quote with: "Honda Pilot - Elite - … smooth ride but feels somewhat like driving a vehicle with a truck frame … KIA - Telluride - … drives like a car, great visibility"
428 QUOTE_FIX: Kia Telluride > Jeep Grand Cherokee L — replace quote with: "Jeep Grand Cherokee L - Limited - Drives like a truck; it is on a RAM 1500 frame … KIA - Telluride - … drives like a car, great visibility"
429 OK: Mercedes GLS > BMW X7 — keep as-is
430 OK: Mercedes GLS > BMW X7 — keep as-is
431 QUOTE_FIX: Mercedes GLS > BMW X7 — replace quote with: "I have a sister who has a gls 450 and one that has an x7 40i. I like the x7 much better. I've driven both, the x7 seems a lot tighter while driving. The Mercedes is a lot more plush and is a bit bigger."
432 OK: Mercedes GLS > BMW X5 — keep as-is
433 RECODE: Range Rover > BMW X7 — evidence test_drove_both → owned_one_td_other
434 OK: Range Rover > BMW X7 — keep as-is [model not named — thread inference]
435 OK: BMW X7 > Range Rover — keep as-is
436 OK: Jeep Grand Wagoneer > Lincoln Navigator — keep as-is
437 OK: Lincoln Navigator > Jeep Grand Wagoneer — keep as-is
438 RECODE: Lincoln Navigator > Jeep Grand Wagoneer — evidence test_drove_both → owned_one_rode_other
439 RECODE: Lincoln Navigator > Jeep Grand Wagoneer — evidence owned_one_td_other → opinion_plus_drive
440 RECODE: GMC Yukon > Jeep Grand Wagoneer — evidence owned_one_td_other → opinion_plus_drive
441 OK: Jeep Grand Wagoneer > Chevrolet Suburban — keep as-is
442 OK: Jeep Grand Wagoneer > GMC Yukon — keep as-is
443 RECODE: Jeep Grand Wagoneer > Chevrolet Suburban — evidence test_drove_both → opinion_plus_drive
444 OK: Cadillac Escalade > Lincoln Navigator — keep as-is
445 OK: GMC Yukon > Lincoln Navigator — keep as-is [model not named — thread inference]
446 OK: Infiniti QX80 > Toyota Sequoia — keep as-is
447 QUOTE_FIX: Lexus GX 550 > Toyota 4Runner — replace quote with: "The seat position always created leg pain on longer trips… The comfort is amazing especially with the massage seats"
448 OK: Lexus GX 550 > Toyota 4Runner — keep as-is
449 OK: Lexus GX 550 > Toyota 4Runner — keep as-is [model not named — thread inference]
450 OK: Lexus GX 550 > Toyota 4Runner — keep as-is
451 RECODE: Toyota 4Runner > Lexus GX 550 — evidence test_drove_both → owned_one_family
452 RECODE: Lexus GX > Lexus GX 550 — evidence owned_one_rode_other → test_drove_both
453 QUOTE_FIX: Lexus GX 550 > Toyota Land Cruiser — replace quote with: "GX (Overtrail, I think) — Nice interior, quiet cabin… LandCruiser (Premium, whatever…the nice one) — Noiser than the GX… Tons of wind noise!!!"
454 QUOTE_FIX: Lexus GX 550 > Toyota 4Runner — replace quote with: "4Runner (Limited and OR Premium) — Quieter than the LC, louder than the GX."
455 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
456 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
457 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
458 OK: GMC Yukon > Cadillac Escalade IQ — keep as-is
459 UNVERIFIED: Lincoln Nautilus > Jeep Grand Cherokee — page unreachable; keep as-is; re-audit when fetchable
460 UNVERIFIED: Mercedes GLC > Cadillac XT5 — page unreachable; keep as-is; re-audit when fetchable
461 UNVERIFIED: BMW X5 > Lexus RX — page unreachable; keep as-is; re-audit when fetchable
462 UNVERIFIED: Audi Q5 > BMW X3 — page unreachable; keep as-is; re-audit when fetchable
463 QUOTE_FIX: Lincoln Navigator > Cadillac Escalade — replace quote with: "I moved from the Cadillac Escalade to the Lincoln Navigator and I am so happy I did. The seats are so amazingly comfortable… It drives so smooth and has so many wonderful features!"
464 UNVERIFIED: Audi Q5 > BMW X3 — page unreachable; keep as-is; re-audit when fetchable; quote names SQ5 not Q5 — confirm coding at re-audit
465 UNVERIFIED: Mercedes GLE > Audi Q5 — page unreachable; keep as-is; re-audit when fetchable
466 UNVERIFIED: Volvo XC60 > Mercedes GLC — page unreachable; keep as-is; re-audit when fetchable
467 UNVERIFIED: Mercedes GLE > BMW X5 — page unreachable; keep as-is; re-audit when fetchable
468 UNVERIFIED: Range Rover Sport > Mercedes GLE — page unreachable; keep as-is; re-audit when fetchable
469 UNVERIFIED: Audi Q5 > Volvo XC60 — page unreachable; keep as-is; re-audit when fetchable; quote never names "Audi Q5"; seats axis not directly stated — recheck at re-audit
470 UNVERIFIED: Audi Q5 > Mercedes GLC — page unreachable; keep as-is; re-audit when fetchable
471 UNVERIFIED: Audi Q5 > BMW X3 — page unreachable; keep as-is; re-audit when fetchable
472 OK: Cadillac XT6 > Acura MDX — keep as-is
473 OK: Buick Enclave > Cadillac XT6 — keep as-is
474 UNVERIFIED: Volkswagen Atlas > Nissan Murano — page unreachable; keep as-is; re-audit when fetchable
475 UNVERIFIED: Nissan Pathfinder > Honda Pilot — page unreachable; keep as-is; re-audit when fetchable
476 OK: Mercedes GLC > Tesla Model X — keep as-is
477 OK: Mercedes GLS > BMW X7 — keep as-is
478 RECODE: Mercedes GLS > BMW X7 — evidence test_drove_both → owned_one_td_other
479 OK: Cadillac Escalade > BMW X7 — keep as-is
480 OK: Range Rover > BMW X7 — keep as-is [model not named — thread inference]
481 OK: Mercedes GLS > BMW X7 — keep as-is [model not named — thread inference]
482 RECODE: Mercedes GLS > BMW X7 — evidence test_drove_both → owned_one_td_other
483 OK: BMW X7 > BMW X5 — keep as-is
484 OK: Mercedes GLS > BMW X7 — keep as-is
485 OK: Mercedes GLS > BMW X7 — keep as-is
486 OK: Lexus LX > Toyota Sequoia — keep as-is
487 OK: Jeep Grand Wagoneer > Lincoln Navigator — keep as-is [model not named — thread inference]
488 OK: Cadillac Escalade > Lincoln Navigator — keep as-is
489 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
490 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
491 OK: Mercedes GLS > Mercedes GLE — keep as-is
492 OK: Cadillac Escalade > Mercedes GLS — keep as-is
493 OK: BMW X7 > BMW X5 — keep as-is
494 OK: BMW X7 > BMW X5 — keep as-is
495 OK: Toyota Sequoia > Chevrolet Tahoe — keep as-is
496 OK: Lexus GX > Mercedes GLS — keep as-is
497 OK: Lexus GX > Infiniti QX80 — keep as-is
498 OK: Lexus GX > BMW X5 — keep as-is
499 OK: Mercedes GLE > BMW X5 — keep as-is
500 RECODE: Genesis GV80 > BMW X5 — evidence test_drove_both → owned_one_td_other
501 OK: Genesis GV80 > Lincoln Aviator — keep as-is
502 RECODE: Lexus TX > Lexus GX 550 — home_team 0 → 1
503 RECODE: Lexus TX > Lexus GX — evidence test_drove_both → owned_one_td_other
503 RECODE: Lexus TX > Lexus GX — home_team 0 → 1
504 RECODE: Lexus GX > Lexus TX — evidence test_drove_both → owned_one_td_other
504 RECODE: Lexus GX > Lexus TX — home_team 0 → 1
505 RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
505 RECODE: Land Rover Defender > Lexus GX 550 — home_team 0 → 1
506 OK: Land Rover Defender > Lexus GX 550 — keep as-is
507 OK: Volvo XC90 > Land Rover Defender — keep as-is
508 OK: Volvo XC90 > Rivian R1S — keep as-is
509 OK: Volvo XC90 > Rivian R1S — keep as-is
510 OK: Acura MDX > Rivian R1S — keep as-is
511 OK: Genesis GV80 > Rivian R1S — keep as-is
512 QUOTE_FIX: Tesla Model X > Rivian R1S — replace quote with: "Its just a much smoother drive… Quieter… More comfortable seats for long trips… The Rivian has its place, but for 99% of the time for me, the MXP is better."
513 OK: Mercedes EQS SUV > BMW iX — keep as-is [model not named — thread inference]
514 OK: Mercedes EQS SUV > BMW iX — keep as-is
515 RECODE: BMW iX > BMW X5 — evidence test_drove_both → owned_one_td_other
516 RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
517 RECODE: Lincoln Aviator > Lexus TX — evidence test_drove_both → owned_one_td_other
517 RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
518 OK: Audi Q8 > BMW X5 — keep as-is
519 OK: BMW X5 > Audi Q8 — keep as-is
520 OK: Audi Q8 > BMW X5 — keep as-is
521 RECODE: Porsche Cayenne > BMW X5 — evidence test_drove_both → owned_one_td_other
522 RECODE: Genesis GV70 > Lincoln Nautilus — evidence test_drove_both → owned_one_td_other
523 OK: Lincoln Nautilus > Genesis GV70 — keep as-is
524 OK: Lexus RX > Genesis GV70 — keep as-is
525 OK: Genesis GV70 > Lexus NX — keep as-is [model not named — thread inference]
526 RECODE: Lexus NX > Genesis GV70 — evidence test_drove_both → owned_one_td_other
527 OK: Volvo XC60 > Lexus NX — keep as-is
528 RECODE: Lexus NX > Toyota RAV4 — evidence test_drove_both → opinion_plus_drive
529 OK: Lincoln Corsair > Lexus NX — keep as-is
530 RECODE: Volkswagen Tiguan > Toyota RAV4 — home_team 0 → 1
531 RECODE: Volkswagen Tiguan > Honda CR-V — evidence test_drove_both → owned_one_td_other
531 RECODE: Volkswagen Tiguan > Honda CR-V — home_team 0 → 1
532 OK: Toyota RAV4 > Volkswagen Tiguan — keep as-is
533 OK: Lincoln Nautilus > Volkswagen Tiguan — keep as-is
534 OK: Mazda CX-9 > Mazda CX-50 — keep as-is
535 OK: Mazda CX-9 > Mazda CX-50 — keep as-is
536 OK: Lexus NX > BMW X1 — keep as-is
537 RECODE: BMW X3 > BMW X1 — evidence test_drove_both → owned_one_td_other
538 OK: Porsche Macan > BMW X3 — keep as-is
539 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
540 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
541 RECODE: Kia Telluride > Kia Sorento — home_team 0 → 1
542 RECODE: Kia Telluride > Kia Sorento — home_team 0 → 1
543 OK: Toyota Highlander > Honda Pilot — keep as-is
544 OK: Buick Enclave > Hyundai Palisade — keep as-is
545 OK: Hyundai Palisade > Buick Enclave — keep as-is
546 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
547 RECODE: Honda Pilot > Jeep Grand Cherokee L — evidence test_drove_both → owned_one_td_other
548 OK: Volkswagen Atlas > Kia Telluride — keep as-is [model not named — thread inference]
549 OK: Volkswagen Atlas > Kia Telluride — keep as-is
550 RECODE: Volkswagen Atlas > Kia Telluride — evidence test_drove_both → owned_one_td_other
551 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
552 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
553 RECODE: Nissan Pathfinder > Honda Passport — evidence test_drove_both → owned_one_td_other
554 OK: Honda Passport > Toyota 4Runner — keep as-is
555 OK: Honda Passport > Toyota 4Runner — keep as-is [model not named — thread inference]
556 OK: Honda Passport > Toyota 4Runner — keep as-is [model not named — thread inference]
557 RECODE: Honda Pilot > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
558 OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
559 OK: Volkswagen Atlas > Hyundai Palisade — keep as-is
560 OK: Kia Telluride > Toyota 4Runner — keep as-is [model not named — thread inference]
561 OK: Hyundai Palisade > Honda Pilot — keep as-is
562 OK: Lexus GX 550 > Toyota Land Cruiser — keep as-is [model not named — thread inference]
563 OK: Lexus GX 550 > Toyota Land Cruiser — keep as-is [model not named — thread inference]
564 OK: Lexus GX > Lexus GX 550 — keep as-is [model not named — thread inference]
565 OK: Lexus GX > Volvo XC90 — keep as-is
566 OK: Lexus LX > Toyota Sequoia — keep as-is
566 RECODE: Lexus LX > Toyota Sequoia — home_team 0 → 1
567 OK: Lexus TX > Toyota Sequoia — keep as-is
567 RECODE: Lexus TX > Toyota Sequoia — home_team 0 → 1
568 RECODE: Lexus LX > Toyota Sequoia — evidence owned_one_family → opinion_plus_drive
568 RECODE: Lexus LX > Toyota Sequoia — home_team 0 → 1
569 RECODE: Buick Enclave > Lexus TX — evidence test_drove_both → owned_one_td_other
570 RECODE: Toyota Sequoia > Lexus LX — home_team 0 → 1
571 OK: Toyota 4Runner > Lexus GX 550 — keep as-is [model not named — thread inference]
572 RECODE: Lexus GX 550 > Jeep Grand Cherokee L — evidence owned_one_td_other → owned_one_rode_other
573 RECODE: Lexus LX > Lexus GX 550 — home_team 1 → 0
574 OK: Mercedes GLS > Lexus GX 550 — keep as-is
575 UNVERIFIED: Lexus GX > Toyota Land Cruiser — page unreachable; keep as-is; re-audit when fetchable
576 OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is
577 OK: Lexus GX > Acura MDX — keep as-is
578 OK: Cadillac Escalade > GMC Yukon — keep as-is
579 OK: GMC Yukon > Cadillac Escalade — keep as-is [model not named — thread inference]
580 QUOTE_FIX: Cadillac Escalade > GMC Yukon — replace quote with: "I like the button on the Yukon for air. Road noise is better in Escalade but I have a lift and 24s on Yukon. I just think overall specs with the Yukon are just easier with kids!"
581 OK: Lincoln Navigator > Jeep Grand Wagoneer — keep as-is
582 OK: Cadillac Escalade > Jeep Grand Wagoneer — keep as-is
583 RECODE: Jeep Grand Wagoneer > GMC Yukon — evidence owned_one_td_other → owned_one_family
584 OK: Jeep Grand Wagoneer > Chevrolet Tahoe — keep as-is
585 RECODE: Chevrolet Tahoe > Lexus GX 550 — evidence owned_one_td_other → opinion
586 OK: Buick Enclave > Cadillac XT6 — keep as-is [model not named — thread inference]
587 OK: Cadillac Escalade IQ > Lincoln Navigator — keep as-is
588 OK: GMC Yukon > Chevrolet Suburban — keep as-is
589 OK: GMC Yukon > Chevrolet Suburban — keep as-is
590 OK: GMC Yukon > Toyota Sequoia — keep as-is
591 QUOTE_FIX: Lincoln Navigator > Toyota Sequoia — replace quote with: "The Sequioa, due to the rear suspension, isn't a smooth ride at all."
592 QUOTE_FIX: Infiniti QX80 > Cadillac Escalade — replace quote with: "I personally didn't like the seats in the Escalade, they seemed very grandma to me. I traded in a the rover and the qx80 was more on par with the Interior to me, just much bigger."
593 OK: Mercedes EQS SUV > BMW iX — keep as-is [model not named — thread inference]
594 RECODE: Mercedes EQS SUV > BMW iX — evidence test_drove_both → owned_one_td_other
595 RECODE: Genesis GV70 > Porsche Macan — evidence test_drove_both → owned_one_td_other
596 OK: Tesla Model X > Rivian R1S — keep as-is
597 OK: Rivian R1S > Tesla Model X — keep as-is
598 OK: Rivian R1S > Tesla Model X — keep as-is
599 OK: Tesla Model X > Rivian R1S — keep as-is
600 OK: Land Rover Defender > Porsche Cayenne — keep as-is
601 OK: Volvo XC90 > Land Rover Defender — keep as-is
602 RECODE: Range Rover Sport > Land Rover Defender — home_team 1 → 0
603 OK: Land Rover Defender > Range Rover Sport — keep as-is
604 OK: Mercedes GLE > Range Rover Sport — keep as-is [model not named — thread inference]
605 RECODE: BMW X5 > Porsche Cayenne — evidence test_drove_both → owned_one_td_other
606 QUOTE_FIX: BMW X5 > Porsche Cayenne — replace quote with: "my wife preferred the smoothnsss of the X5 over the Cayenne"
607 OK: BMW iX > Tesla Model Y — keep as-is
608 OK: Audi Q5 > Porsche Macan — keep as-is [model not named — thread inference]
609 OK: Volvo XC60 > Rivian R1S — keep as-is [model not named — thread inference]
610 RECODE: Honda Pilot > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
611 OK: Honda Pilot > Mazda CX-90 — keep as-is
612 RECODE: Nissan Murano > Nissan Pathfinder — home_team 0 → 1
613 OK: Hyundai Palisade > Volkswagen Atlas — keep as-is
614 OK: Hyundai Palisade > Mazda CX-90 — keep as-is
615 QUOTE_FIX: Mazda CX-90 > Hyundai Palisade — replace quote with: "A few weeks ago, I test drove the Mazda CX-90 PHEV… everything felt smooth and enjoyable… During the Palisade test drive… it felt slow and heavy compared to the Mazda, not as smooth."
616 OK: Hyundai Palisade > Mazda CX-90 — keep as-is
617 RECODE: Nissan Pathfinder > Toyota Highlander — evidence test_drove_both → owned_one_td_other
618 OK: Toyota Highlander > Nissan Pathfinder — keep as-is
619 OK: Nissan Pathfinder > Toyota Highlander — keep as-is
620 RECODE: Nissan Pathfinder > Toyota Highlander — evidence test_drove_both → owned_one_td_other
621 QUOTE_FIX: Honda Pilot > Honda Passport — replace quote with: "Test drove both yesterday. Passport is agile but on highway i think pilot is better and quieter"
622 OK: Honda Pilot > Honda Passport — keep as-is
623 QUOTE_FIX: Kia Telluride > Kia Sorento — replace quote with: "Space would be better in the Telluride… I had a Sorento and the 3rd row seats were useless"
624 OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
625 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
626 RECODE: Honda Pilot > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
627 RECODE: Hyundai Palisade > Buick Enclave — evidence test_drove_both → owned_one_td_other
628 OK: Volkswagen Atlas > Honda Pilot — keep as-is
629 OK: Tesla Model X > Tesla Model Y — keep as-is
630 OK: Tesla Model X > Tesla Model Y — keep as-is
631 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
632 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
633 OK: Subaru Outback > Subaru Crosstrek — keep as-is
634 OK: Subaru Outback > Subaru Crosstrek — keep as-is
635 RECODE: Subaru Outback 2026 > Subaru Forester — evidence test_drove_both → owned_one_td_other
635 RECODE: Subaru Outback 2026 > Subaru Forester — home_team 0 → 1
636 OK: Lincoln Corsair > Lexus NX — keep as-is [model not named — thread inference]
637 OK: Audi Q5 > Lincoln Corsair — keep as-is
638 OK: Lincoln Corsair > Mercedes GLC — keep as-is
639 QUOTE_FIX: Genesis GV70 > Audi Q5 — replace quote with: "I ended up with the Q5 (somewhat begrudgingly) after trying it along with the X3, XC60, GV70… GV70 was most comfortable by a decent margin with the Volvo in second"
639 RECODE: Genesis GV70 > Audi Q5 — evidence test_drove_both → owned_one_td_other
640 OK: BMW X3 > BMW X1 — keep as-is
641 OK: Lexus RX > Cadillac XT5 — keep as-is
642 RECODE: Mazda CX-9 > Toyota Highlander — evidence test_drove_both → owned_one_td_other
643 OK: Volkswagen Tiguan > Honda CR-V — keep as-is
644 OK: Volkswagen Tiguan > Honda CR-V — keep as-is
645 OK: Lincoln Nautilus > Lincoln Corsair — keep as-is
646 RECODE: Lincoln Corsair > Lexus NX — evidence test_drove_both → owned_one_td_other
647 RECODE: Cadillac XT6 > BMW X5 — evidence test_drove_both → owned_one_td_other
648 RECODE: Cadillac XT6 > Toyota Highlander — evidence test_drove_both → owned_one_td_other
649 OK: Cadillac XT6 > GMC Yukon — keep as-is
650 OK: Cadillac XT6 > Cadillac XT5 — keep as-is
651 OK: Subaru Crosstrek > BMW X1 — keep as-is
652 UNVERIFIED: GMC Yukon > Cadillac Escalade — page unreachable; keep as-is; re-audit when fetchable
653 UNVERIFIED: Toyota Venza > Toyota RAV4 — page unreachable; keep as-is; re-audit when fetchable
654 UNVERIFIED: Toyota Highlander > Toyota Venza — page unreachable; keep as-is; re-audit when fetchable
655 UNVERIFIED: Subaru Crosstrek > Honda CR-V — page unreachable; keep as-is; re-audit when fetchable
656 OK: Mazda CX-9 > Toyota RAV4 — keep as-is
657 OK: GMC Yukon > Rivian R1S — keep as-is
658 OK: GMC Yukon > Rivian R1S — keep as-is
659 OK: GMC Yukon > Rivian R1S — keep as-is
660 OK: GMC Yukon > Rivian R1S — keep as-is
661 OK: GMC Yukon > Rivian R1S — keep as-is
662 OK: Rivian R1S > Chevrolet Suburban — keep as-is
663 OK: Toyota Sequoia > Chevrolet Tahoe — keep as-is
664 OK: Infiniti QX80 > Cadillac Escalade — keep as-is
665 OK: Infiniti QX80 > Chevrolet Tahoe — keep as-is
666 OK: GMC Yukon > Toyota Sequoia — keep as-is [model not named — thread inference]
667 OK: GMC Yukon > Range Rover — keep as-is
668 OK: GMC Yukon > Toyota Sequoia — keep as-is
669 RECODE: GMC Yukon > Lexus GX — home_team 0 → 1
670 UNVERIFIED: Cadillac Escalade > Chevrolet Tahoe — page unreachable; keep as-is; re-audit when fetchable
671 UNVERIFIED: Chevrolet Tahoe > Toyota Sequoia — page unreachable; keep as-is; re-audit when fetchable
672 OK: Range Rover > Toyota Sequoia — keep as-is
673 OK: GMC Yukon > Lexus GX — keep as-is
674 QUOTE_FIX: Lexus RX > Lexus GX 550 — replace quote with: "I've test drive both twice. I enjoy both. The GX does ride a little rougher on the same road but that is too be expected."
675 UNVERIFIED: GMC Yukon > Cadillac Escalade — page unreachable; keep as-is; re-audit when fetchable
676 OK: Rivian R1S > Tesla Model X — keep as-is
677 OK: Rivian R1S > Tesla Model X — keep as-is
678 OK: Range Rover Sport > Land Rover Defender — keep as-is
679 OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
680 OK: Range Rover > Land Rover Defender — keep as-is
681 OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
682 OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
683 OK: Range Rover Sport > Land Rover Defender — keep as-is
684 OK: Audi Q5 > Genesis GV70 — keep as-is
685 RECODE: Porsche Cayenne > Mercedes GLE AMG — evidence test_drove_both → owned_one_td_other
686 OK: BMW X5 > Porsche Cayenne — keep as-is
687 OK: Porsche Cayenne > BMW X5 — keep as-is
688 OK: BMW X7 > Porsche Cayenne — keep as-is
689 OK: BMW X5 > Porsche Cayenne — keep as-is
690 OK: Mercedes GLE > BMW X5 — keep as-is
691 OK: Mercedes GLE > Porsche Cayenne — keep as-is
692 OK: Mercedes GLE > BMW X5 — keep as-is
693 RECODE: Mercedes GLE > BMW X5 — evidence test_drove_both → owned_one_td_other
694 OK: BMW X5 > Mercedes GLE — keep as-is
695 DELETE: Mercedes GLE > BMW X5 — remove row
696 RECODE: BMW X5 > Porsche Cayenne — evidence test_drove_both → owned_one_td_other
697 OK: Mercedes GLE > BMW X5 — keep as-is
698 RECODE: Mercedes GLE > Jeep Grand Cherokee — evidence test_drove_both → owned_one_td_other
699 RECODE: Jeep Grand Cherokee > BMW X5 — evidence test_drove_both → owned_one_td_other
700 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
701 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
702 OK: Subaru Outback > Subaru Crosstrek — keep as-is
703 OK: Subaru Outback > Subaru Crosstrek — keep as-is
704 RECODE: Subaru Outback > Subaru Crosstrek — evidence owned_one_loaner → opinion_plus_drive
705 RECODE: Cadillac XT6 > Cadillac XT5 — home_team 0 → 1
706 OK: Tesla Model X > Tesla Model Y — keep as-is
707 OK: Tesla Model X > Tesla Model Y — keep as-is
708 OK: Tesla Model X > Tesla Model Y — keep as-is
709 OK: Tesla Model X > Tesla Model Y — keep as-is
710 RECODE: Lincoln Corsair > Volvo XC60 — evidence test_drove_both → owned_one_td_other
711 OK: Nissan Murano > Nissan Pathfinder — keep as-is [model not named — thread inference]
712 OK: Nissan Murano > Nissan Pathfinder — keep as-is
713 OK: Nissan Pathfinder > Nissan Murano — keep as-is
714 OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
715 OK: Lexus NX > Mazda CX-5 — keep as-is
716 OK: Subaru Outback > Subaru Forester — keep as-is
717 OK: Honda CR-V > Subaru Forester — keep as-is
718 OK: Subaru Forester > Subaru Crosstrek — keep as-is
719 OK: Subaru Forester > Subaru Crosstrek — keep as-is
720 OK: BMW X1 > BMW X3 — keep as-is
720 RECODE: BMW X1 > BMW X3 — home_team 0 → 1
721 OK: Kia Telluride > Toyota RAV4 — keep as-is
722 OK: Volvo XC90 > Tesla Model Y — keep as-is
723 QUOTE_FIX: Mazda CX-90 > Kia Telluride — replace quote with: "The difference in road noise, the power and performance, and comfort are all better."
724 OK: Honda Pilot > Mazda CX-90 — keep as-is
725 OK: Honda Pilot > Mazda CX-90 — keep as-is
726 OK: Honda Pilot > Jeep Grand Cherokee L — keep as-is
727 QUOTE_FIX: Hyundai Palisade > Buick Enclave — replace quote with: "We test drove the Enclave and were not impressed. It's a 4 cylinder engine and the vehicle can't get out of its own way and makes a tom of noise. We were a Buick family until 2026 and now own a Pslisade."
728 OK: Hyundai Palisade > Kia Telluride — keep as-is
729 RECODE: Hyundai Palisade > Kia Telluride — evidence test_drove_both → owned_one_td_other
730 QUOTE_FIX: Kia Telluride > Mazda CX-90 — replace quote with: "Had 2022 Telluride, traded in for 2024 CX-90 PHEV… The only reason I switched from Telluride to CX90 is cost savings… Other than that, Telluride is way more comfortable, more spacious…"
731 OK: Kia Telluride > Toyota 4Runner — keep as-is
732 RECODE: Toyota Grand Highlander > Honda Pilot — evidence test_drove_both → owned_one_td_other
733 OK: Hyundai Palisade > Honda Pilot — keep as-is
734 OK: Kia Telluride > Hyundai Palisade — keep as-is
734 RECODE: Kia Telluride > Hyundai Palisade — home_team 0 → 1
735 OK: Cadillac XT6 > Cadillac XT5 — keep as-is [model not named — thread inference]
736 RECODE: Ford Explorer > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
737 OK: Ford Explorer > Toyota 4Runner — keep as-is
737 RECODE: Ford Explorer > Toyota 4Runner — home_team 0 → 1
738 RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → owned_one_td_other
739 RECODE: Honda Pilot > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
740 OK: Mazda CX-5 > Mazda CX-90 — keep as-is
741 OK: Honda Passport > Honda Pilot — keep as-is
742 UNVERIFIED: Ford Explorer > Toyota Highlander — page unreachable; keep as-is; re-audit when fetchable
743 UNVERIFIED: Toyota Highlander > Ford Explorer — page unreachable; keep as-is; re-audit when fetchable
744 UNVERIFIED: Buick Enclave > Kia Telluride — page unreachable; keep as-is; re-audit when fetchable
745 UNVERIFIED: Buick Enclave > Hyundai Palisade — page unreachable; keep as-is; re-audit when fetchable
746 UNVERIFIED: Mazda CX-9 > Honda Pilot — page unreachable; keep as-is; re-audit when fetchable
747 UNVERIFIED: Mazda CX-9 > Toyota Highlander — page unreachable; keep as-is; re-audit when fetchable
748 UNVERIFIED: Mazda CX-9 > Nissan Pathfinder — page unreachable; keep as-is; re-audit when fetchable
749 OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
750 OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
750 RECODE: Cadillac Escalade IQ > Tesla Model X — home_team 0 → 1
751 OK: Cadillac Escalade IQ > Cadillac Escalade — keep as-is [model not named — thread inference]
752 OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
753 OK: Mercedes GLE AMG > BMW X5 — keep as-is
753 RECODE: Mercedes GLE AMG > BMW X5 — home_team 0 → 1
754 OK: Mercedes GLS > Mercedes GLE AMG — keep as-is
754 RECODE: Mercedes GLS > Mercedes GLE AMG — home_team 0 → 1
755 OK: BMW X5 > Mercedes GLE — keep as-is
756 OK: Lexus GX > Toyota Land Cruiser — keep as-is
756 RECODE: Lexus GX > Toyota Land Cruiser — home_team 0 → 1
757 OK: Toyota 4Runner > Toyota Land Cruiser — keep as-is
758 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
759 QUOTE_FIX: Lexus LX > Toyota Sequoia — replace quote with: "Not apples to apples, but I have a LX 700 and a Sequoia, both 2025s. My wife and I prefer the Lexus while our kids prefer the Sequoia… The biggest differences are noise, ride comfort, and space."
760 OK: Lexus LX > Toyota Land Cruiser — keep as-is [model not named — thread inference]
761 OK: GMC Yukon > Toyota Sequoia — keep as-is
762 QUOTE_FIX: GMC Yukon > Chevrolet Tahoe — replace quote with: "The Yukon entertainment system screen is worlds better than Chevy amd the fit and finish is better to… I also feel the road noise is quieter in the Yukon than Chevy."
763 QUOTE_FIX: Range Rover > Land Rover Defender — replace quote with: "I have both. I love my RR much more."
764 OK: Land Rover Defender > Porsche Cayenne — keep as-is
765 OK: Range Rover > Porsche Cayenne — keep as-is [model not named — thread inference]
766 OK: Mercedes GLE > Porsche Cayenne — keep as-is
767 OK: Land Rover Defender > Porsche Cayenne — keep as-is
768 OK: Jeep Grand Cherokee > BMW X5 — keep as-is
768 RECODE: Jeep Grand Cherokee > BMW X5 — home_team 0 → 1
769 OK: BMW X5 > Tesla Model Y — keep as-is
770 OK: Jeep Grand Cherokee > Tesla Model Y — keep as-is
771 OK: Land Rover Defender > Rivian R1S — keep as-is
772 OK: BMW X5 > Rivian R1S — keep as-is
773 OK: BMW iX > Rivian R1S — keep as-is [model not named — thread inference]
774 RECODE: Genesis GV70 > Porsche Macan — evidence test_drove_both → owned_one_td_other
774 RECODE: Genesis GV70 > Porsche Macan — home_team 0 → 1
775 RECODE: Porsche Macan > Audi Q5 — evidence test_drove_both → owned_one_td_other
776 RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
777 OK: Volkswagen Tiguan > Honda CR-V — keep as-is
777 RECODE: Volkswagen Tiguan > Honda CR-V — home_team 0 → 1
778 OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is
778 RECODE: Volkswagen Tiguan > Toyota RAV4 — home_team 0 → 1
779 OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
779 RECODE: Volkswagen Tiguan > Mazda CX-5 — home_team 0 → 1
780 OK: Toyota Venza > Toyota RAV4 — keep as-is
780 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
781 OK: Toyota Venza > Toyota RAV4 — keep as-is
781 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
782 OK: Lincoln Nautilus > Lincoln Corsair — keep as-is
782 RECODE: Lincoln Nautilus > Lincoln Corsair — home_team 0 → 1
783 OK: Mercedes GLC > BMW X3 — keep as-is
783 RECODE: Mercedes GLC > BMW X3 — home_team 0 → 1
784 OK: Honda CR-V > Subaru Crosstrek — keep as-is
785 OK: Subaru Crosstrek > Subaru Forester — keep as-is
785 RECODE: Subaru Crosstrek > Subaru Forester — home_team 0 → 1
786 OK: BMW X3 > BMW X1 — keep as-is
786 RECODE: BMW X3 > BMW X1 — home_team 0 → 1
787 OK: BMW X5 > BMW X1 — keep as-is
787 RECODE: BMW X5 > BMW X1 — home_team 0 → 1
788 OK: BMW X5 > BMW X3 — keep as-is
788 RECODE: BMW X5 > BMW X3 — home_team 0 → 1
789 QUOTE_FIX: Subaru Outback 2026 > Subaru Forester — replace quote with: "The Outback Premium felt more comfortable and more upscale, partly because the Premium trim includes the nicer StarTex interior. It also seemed better for road trips and family cargo."
789 RECODE: Subaru Outback 2026 > Subaru Forester — home_team 0 → 1
790 QUOTE_FIX: Subaru Outback > Subaru Forester — replace quote with: "For me it's the ride quality and handling. Forester is nice for short trips. Outback is nice for long trips. The Outback has way more comfortable seats imo."
790 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
791 OK: Nissan Murano > Tesla Model X — keep as-is
791 RECODE: Nissan Murano > Tesla Model X — home_team 0 → 1
792 UNVERIFIED: Buick Enclave > BMW X5 — page unreachable; keep as-is; re-audit when fetchable
793 UNVERIFIED: Jeep Grand Cherokee L > Hyundai Palisade — page unreachable; keep as-is; re-audit when fetchable
794 UNVERIFIED: Jeep Grand Cherokee L > Kia Telluride — page unreachable; keep as-is; re-audit when fetchable
795 UNVERIFIED: Cadillac XT5 > BMW X3 — page unreachable; keep as-is; re-audit when fetchable
796 QUOTE_FIX: Mercedes EQS SUV > BMW iX — replace quote with: "We've had both-a 2023 EQS suv and our 2025 iX50. … Seats are legit terrible … Seats were incredible-massages, pillows etc"
797 OK: Mercedes EQS SUV > Rivian R1S — keep as-is
798 OK: Subaru Crosstrek > Subaru Outback — keep as-is
799 OK: Subaru Outback > Subaru Crosstrek — keep as-is
800 OK: Cadillac Escalade IQ > Cadillac Escalade — keep as-is
801 RECODE: Range Rover > Land Rover Defender — evidence test_drove_both → owned_one_td_other
802 OK: BMW X5 > Tesla Model Y — keep as-is
803 OK: BMW X5 > Tesla Model Y — keep as-is
804 OK: Land Rover Defender > Rivian R1S — keep as-is
805 OK: BMW X5 > Rivian R1S — keep as-is
806 OK: Porsche Macan > Audi Q5 — keep as-is
807 RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
808 OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
808 RECODE: Volkswagen Tiguan > Mazda CX-5 — home_team 0 → 1
809 OK: Toyota Venza > Toyota RAV4 — keep as-is
809 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
810 RECODE: Toyota Venza > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
810 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
811 OK: Toyota Venza > Toyota RAV4 — keep as-is
811 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
812 OK: Toyota Venza > Toyota RAV4 — keep as-is
812 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
813 RECODE: Lincoln Nautilus > Lincoln Corsair — evidence test_drove_both → owned_one_td_other
813 RECODE: Lincoln Nautilus > Lincoln Corsair — home_team 0 → 1
814 OK: Mercedes EQS SUV > BMW iX — keep as-is
815 RECODE: Mercedes EQS SUV > Rivian R1S — evidence test_drove_both → owned_one_td_other
816 OK: Range Rover > Mercedes GLS — keep as-is [model not named — thread inference]
817 QUOTE_FIX: Audi Q7 > BMW X5 — replace quote with: "I test drove the X5 and Q7 today and the X5 LOOKS better but the Q7 FEELS better"
818 QUOTE_FIX: Genesis GV80 > BMW X5 — replace quote with: "I've driven all three and in the end we went with the x5m50i because of the performance Factor. … Gv80 was a little cushier than we preferred"
818 RECODE: Genesis GV80 > BMW X5 — evidence test_drove_both → owned_one_td_other
819 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "The Hybrid Palisade, though was a completely different animal. … But the real showstopper is the ride quality. The chassis just glides over bumps and imperfections; it truly soaks everything up. My old Tucson and even the santafe I test drove would feel jittery on these same roads."
820 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "The Palisade drives wonderfully and is quiet, while the Santa Fe is more sporty but still smooth and quiet."
821 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "We did 2 test drives with each and were sold by the Palisade (2026) easily. … The ride is much, much smoother as well. The Santa Fe feels zippy to drive, but you feel every bump on the road."
821 RECODE: Hyundai Palisade > Hyundai Santa Fe — evidence test_drove_both → owned_one_td_other
822 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "It's comfortable just the right size. … Palisade is also very nice. Quieter and smoother but not by too much."
823 QUOTE_FIX: Ford Expedition > Chevrolet Suburban — replace quote with: "the Yukon and Suburban (we owned a Suburban, rented a Yukon Denali for a week to get a feel before buying the Expedition) just drove like they were too top heavy and about to tip on any curve going over 55… The Expedition grips the road and you just feel steady and more level"
824 QUOTE_FIX: Chevrolet Suburban > Ford Expedition — replace quote with: "The Suburban rides smoother and softer, handles better… Chevy uses MUCH better tires (Michelin Primacy) than Ford (hankook Dynapro ATM) on the examples I've rented. Those dynapros are loud!!"
825 QUOTE_FIX: Ford Expedition > Chevrolet Tahoe — replace quote with: "When sitting in the expy the seats are noticeably better. I did not get to test drive a max so not sure the ride quality compared to standard. I prefer the looks of the Tahoe and features of the expedition."
826 QUOTE_FIX: Cadillac Escalade > Ford Expedition — replace quote with: "It felt like I was driving a van—every bump in the road was noticeable. Compared to my Escalade, which has a much smoother ride, the Expedition's suspension felt rough and unrefined."
827 QUOTE_FIX: Lincoln Navigator > Ford Expedition — replace quote with: "I test drove a bunch of different exp trims… I decided on a navigator L reserve trim w/ luxury package and it's a much better driving experience than a platinum trim expedition."
827 RECODE: Lincoln Navigator > Ford Expedition — evidence test_drove_both → owned_one_td_other
828 QUOTE_FIX: Ford Expedition > Chevrolet Suburban — replace quote with: "the interior is nicer and much more comfortable. I won't knock the GMs i had, they were good vehicles but we gambled on a switch to the expedition and my wife wishes we would have done it sooner."
