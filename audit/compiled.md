# Compiled audit — one line per verdict (applied to `data/comparisons.csv`)
Each line: `<id> <TAG>: <winner> > <loser> — <action>`; id = brief random id from the CSV `id` column (stable across row deletes). Tags: OK keep / QUOTE_FIX replace quote / RECODE change field / DELETE remove row / UNVERIFIED re-audit when fetchable. Upvotes intentionally untouched (planned for removal). DELETE / QUOTE_FIX / RECODE lines have been applied.
w6cq DELETE: Lincoln Aviator > Lexus RX — remove row
qur7 QUOTE_FIX: Lincoln Aviator > Lincoln Corsair — add parent/thread context: "I have one- they're huge. I think one of the smaller cheaper Lincolns would be better for a single person. They don't ride as nice, and aren't built as well though."
qur7 RECODE: Lincoln Aviator > Lincoln Corsair — evidence owned_one_td_other → opinion
p42y OK: Lexus RX > Audi A7 — keep as-is; fuller quote suggested: "I've had a current gen RX and a last gen Audi A7, the Lexus was quieter and more softly sprung - was like being in a bank vault."
dsu7 OK: Volvo XC60 > Mazda CX-5 — keep as-is; fuller quote suggested: "Love my CX5, but got a XC-60 last year and that wins hands down if you can stretch the budget. Most comfortable seats I've tried of any brand."
b2mz OK: Honda CR-V > Subaru Outback — keep as-is; fuller quote suggested: "It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V Hybrid, and we've been thrilled."
cfj8 QUOTE_FIX: Honda CR-V > Mazda CX-50 — replace quote with: "It's the CR-V, hands down. We test drove all of these and went with a 2025 CR-V Hybrid, and we've been thrilled."
m25u OK: Subaru Outback > Honda CR-V — keep as-is; fuller quote suggested: "Outback is much more comfortable. Drive the others over a bad road with potholes and you will feel the difference. Avoid Crv and Mazda. There are plenty of much more comfortable options."
j6ae OK: Subaru Outback > Mazda CX-5 — keep as-is; fuller quote suggested: "Outback is much more comfortable. Drive the others over a bad road with potholes and you will feel the difference. Avoid Crv and Mazda. There are plenty of much more comfortable options."
w4g9 QUOTE_FIX: Subaru Outback 2026 > Mazda CX-50 — add parent/thread context: "…Boyfriend is pushing heavily to 'size up' to a CX-30…"
w4g9 RECODE: Subaru Outback 2026 > Mazda CX-50 — axis seats → overall
w4g9 RECODE: Subaru Outback 2026 > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
r9vk DELETE: Honda CR-V > Mazda CX-5 — remove row
v24d OK: Toyota Venza > Subaru Outback — keep as-is; fuller quote suggested: "For real. Venza is a nice blend of luxury and the seats and road noise are a world of difference if you don't need the trunk space of the Outback or crv"
hk2s OK: Toyota Venza > Honda CR-V — keep as-is; fuller quote suggested: "For real. Venza is a nice blend of luxury and the seats and road noise are a world of difference if you don't need the trunk space of the Outback or crv"
vhc5 OK: BMW X5 > Honda CR-V — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
ntp4 OK: BMW X5 > Lexus RX — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
bg6j OK: BMW X5 > Toyota RAV4 — keep as-is; fuller quote suggested: "Answer is a used BMW X5 from 2021-2023… My brother has a 2022 RX350. My neighbor has the 2024 RAV4. Girlfriend's sister has the CR-V. All of them prefer the X5 if we're together and doing a bigger grocery haul, a longer road trip (2+ hours one way), or are going out together with 3 in the backseat."
b5p5 DELETE: Lexus RX > Cadillac XT5 — remove row
s2qn QUOTE_FIX: Lincoln Nautilus > Cadillac XT5 — replace quote with: "XT5 is a lazy money grab by GM, it doesn't ride as well as you might expect. … Look for and test drive a USED (high initial depreciation) 2024 model year Lincoln NAUTILUS - Nautilus has a soft suspension tune"
z4c2 RECODE: Lexus RX > Lexus NX — evidence owned_one_td_other → opinion
ex4q DELETE: Lexus RX > Toyota RAV4 — remove row
zd4y OK: Volvo XC60 > Toyota RAV4 — keep as-is; fuller quote suggested: "I went from rav4 to an xc60. I could never get comfortable in the rav and after an hour I was over it. Can drive the volvo all day with no discomfort."
x453 OK: Volvo XC60 > Toyota RAV4 — keep as-is; fuller quote suggested: "Oh cool, a post I can actually chime in on! Have had a RAV4 for 7 years now with my wife, and it's great. … Tried a 2023 XC60 Plus Bright Theme, and I immediately knew it was the right choice. It is undoubtedly the most comfortable car I have driven in thus far and can drive long periods without any discomfort. … We are incredibly happy with it, and despite her trying to pretend otherwise, she drives it far more than her Rav4 now."
v4ar OK: Volvo XC60 > Mazda CX-50 — keep as-is; fuller quote suggested: "…2 of my friends have them and I've ridden in both (cx50) and they weren't bad imo. Not as comfortable as our xc60 Volvos or GMC Sierra."
jzk5 OK: Volvo XC60 > BMW X3 — keep as-is; fuller quote suggested: "When I looked, it was between this and the BMW X1/X3. Both better than the Rav. The Volvo is more comfortable but the BMW infotainment was much better. I leaned more towards BMW but try it out yourself."
cv8b QUOTE_FIX: Audi Q5 > Volvo XC60 — replace quote with: "Just bought a Q5, both seat options are nice… The Volvo seats were slightly better than the Audi. When I test drove the XC60 i think it either had 20" wheels or run flats because it rode like shit. Small bumps were fine but bigger bumps and pot holes felt worse than in my GTI… The Q5 is definitely firmer than I think a crossover should be but it drives like a normal car and feels much better to drive than the XC60…"
yd7s RECODE: Audi Q5 > Volvo XC60 — evidence test_drove_both → opinion
mwu2 OK: Porsche Macan > Volvo XC60 — keep as-is; fuller quote suggested: "The xc60 for having such good NVH and seats does not have super soft suspension. I found that the air suspension optioned Macan and Q5 were way more comfortable ride wise than the XC60, especially the Macan since they offer 14 and 18 way adjustable seats."
nn8d OK: Audi Q5 > Volvo XC60 — keep as-is; fuller quote suggested: "The xc60 for having such good NVH and seats does not have super soft suspension. I found that the air suspension optioned Macan and Q5 were way more comfortable ride wise than the XC60, especially the Macan since they offer 14 and 18 way adjustable seats."
uh8k DELETE: Mercedes GLC > Volvo XC60 — remove row
kz3s RECODE: Mercedes GLC > Volvo XC60 — evidence opinion_plus_drive → opinion
y4yc OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is; fuller quote suggested: "My wife and I recently test drove 8 different vehicles in the RAV4 size category. My whole family found the new Tiguan to be the most comfortable by far. VW wasn't on our short list, but the interior sold us."
t4w2 DELETE: Lincoln Nautilus > Volvo XC60 — remove row
ec3t OK: Volvo XC60 > Lexus RX — keep as-is; fuller quote suggested: "At different price points / Xc60 / Lexus Rx / Toyota crown signia. The rx is not even on the same spectrum as the Volvo"
v8ax OK: Range Rover Sport > Porsche Cayenne — keep as-is; fuller quote suggested: "2023 Porsche Cayenne- Too Sporty- felt the road too much, love the look but the ride is far too uncomfortable. 2024-Range Rover Sport - Don't like how the outside looks, the SUV drives like a dream- I test drove it just because I was curious but with the horror stories about range rovers - I'll pass"
edp9 OK: Porsche Cayenne > Porsche Cayenne — keep as-is; editorial exclusion marker (wt=0); optionally move marker text out of quote column
ww3m OK: Mercedes GLE > Lexus GX — keep as-is; fuller quote suggested: "Not sure about the newer mercedes, but I have a 19 Lexus GX and my wife has a 14 mercedes ml350, and the benz wins in the luxury ride and comfort hands down. In fairness, the lexus is an old fashion body on frame and way more capable offroad, but for long trips the merc is the clear winner."
ft57 RECODE: Lincoln Aviator > BMW X5 — evidence opinion_plus_drive → opinion
ft57 QUOTE_FIX: Lincoln Aviator > BMW X5 — add parent/thread context: "You should test drive a Volvo XC90. Especially with the X5's multi-contour seat option: [marketing copy]. That seat is the bomb. You can make it a Lazy Boy on the road. Best car seat ever"
m3cu RECODE: BMW X7 > BMW X5 — evidence owned_both → owned_one_td_other
y452 RECODE: Audi Q7 > Audi Q8 — evidence test_drove_both → opinion
y23c OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I own a 2022 GLE 450 and a 2025 x5 m60i. The GLE is a dramatically smoother ride and is my choice for a road trip, despite having only 1 inch smaller wheels and having the base suspension. … The ride [of the X5] is much rougher than I was expecting…"
q6gh OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I have both cars. I drive X5 hybrid and my wife has GLE 350. I think the X5 has better engine performance/ response and maneuvering. But Mercedes is larger and more comfortable on longer trips."
h8an OK: Mercedes GLE > BMW X5 — keep as-is
h8an RECODE: Mercedes GLE > BMW X5 — weight_base 1.5 → 3.0
mu7c OK: Mercedes GLE > BMW X5 — keep as-is
tk8a OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I was pretty torn between the 2 and ended up buying the X5. The merc seemed quieter and smoother to drive but also lacked anything that I would consider fun. I was in the 4 cylinder 350 though. … The bmw just felt much more connected to the road…"
mu2m OK: BMW X5 > Mercedes GLE — keep as-is
s787 DELETE: BMW X5 > Mercedes GLE — remove row
jv5t OK: Mercedes GLE > BMW X5 — keep as-is; fuller quote suggested: "I have had both and currently have the X5. … I do miss the merc seats but the BMW are nice too. Felt the Benz seats were buttery and plush. Space in the rear - Benz is bigger for 2nd row and cargo."
b98s RECODE: BMW X5 > Mercedes GLE — evidence test_drove_both → owned_one_td_other
y3yk OK: BMW X5 > Mercedes GLE — keep as-is; fuller quote suggested: "I'm not a BMW guy. This X5 is my first one. I test drove all the foreign luxury mid size SUVs with an open mind. … That said, with the inexpensive Multi contour seats option, the X5 seats are more comfortable and adjustable than anything else I tried, including the highest end Cayenne seats. The Merc seats are ok, but nothing special in the segment."
b6zb OK: BMW X5 > Porsche Cayenne — keep as-is; fuller quote suggested: "I'm not a BMW guy. This X5 is my first one. I test drove all the foreign luxury mid size SUVs with an open mind. … That said, with the inexpensive Multi contour seats option, the X5 seats are more comfortable and adjustable than anything else I tried, including the highest end Cayenne seats. The Merc seats are ok, but nothing special in the segment."
bfa4 RECODE: BMW X5 > Mercedes GLE — evidence test_drove_both → owned_both
v6yu RECODE: Volvo XC90 > Land Rover Defender — evidence owned_both → opinion
n5vp OK: Volvo XC90 > Land Rover Defender — keep as-is; fuller quote suggested: "I traded in my 2023 XC90 when the lease ended for a 2025 Land Rover Defender 110. Two different vehicles for sure, but I miss the subtlety of the Volvo and the ergonomics of that car. It was so comfortable to drive!"
d7zc OK: Volvo XC90 > Rivian R1S — keep as-is
bz2w OK: BMW X5 > Volvo XC90 — keep as-is; fuller quote suggested: "I test drove the XC90, Lincoln Aviator, and BMW X5. I chose the X5. … The air suspension was great but still felt bulky. The X5 was an amazing blend of comfort and sporty handling, and I fell in love with it."
mt8k RECODE: Volvo XC90 > BMW X5 — evidence owned_both → test_drove_both
mt8k RECODE: Volvo XC90 > BMW X5 — weight 1.5 → 2.0
ucf6 OK: BMW X7 > Volvo XC90 — keep as-is; fuller quote suggested: "I moved on to an X7 M50i and EQS SUV after having an XC90 for 7yrs. … The biggest issue I had with the car … is the lack of noise insulation. … it just felt noisy inside. … When I got my X7, it was worlds better where I felt like I could have a quiet conversation in the car even when the v8 is cranking and the EQS took it another step up in serene-ness."
sw23 OK: Mercedes EQS SUV > Volvo XC90 — keep as-is; fuller quote suggested: "I moved on to an X7 M50i and EQS SUV after having an XC90 for 7yrs. … The biggest issue I had with the car … is the lack of noise insulation. … it just felt noisy inside. … When I got my X7, it was worlds better where I felt like I could have a quiet conversation in the car even when the v8 is cranking and the EQS took it another step up in serene-ness."
czp3 OK: Volvo XC90 > BMW X7 — keep as-is
u2jk QUOTE_FIX: Volvo XC90 > Mercedes GLE — replace quote with: "but I've had a '24 GLE350 as a service loaner a couple of times and while that does feel a bit more solid and the interior is nicer, I still prefer the XC90."
u2jk RECODE: Volvo XC90 > Mercedes GLE — axis seats → overall
fg67 RECODE: Volvo XC90 > Mercedes GLE — evidence test_drove_both → owned_one_td_other [model not named — thread inference]
fn8r QUOTE_FIX: BMW X5 > Volvo XC90 — replace quote with: "I just came from BMW, which was better in every way. But hopefully the Volvo is more reliable which is what I need right now. …It was more comfy and the ride was nicer on longer drives? … Yes. Bigger engine with a smoother ride."
cg84 DELETE: Volvo XC90 > Audi Q7 — remove row
kj3y OK: Volvo XC90 > Subaru Forester — keep as-is
jw3j OK: Lexus RX > Hyundai Palisade — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
tv6z OK: Lexus RX > Genesis GV80 — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
f6eh OK: Lexus RX > Honda Passport — keep as-is; fuller quote suggested: "I have a 24 RX and a 24 Honda passport and a 25 Kia soul. I've had 23 Genesis GV80 and a 20 Kia sonata and a 21 and 22 Hyundai Palisades. The Lexus is the smoothest of all of them."
rc5y RECODE: Cadillac Escalade > Lexus LX — evidence owned_one_td_other → opinion
rc5y RECODE: Cadillac Escalade > Lexus LX — home_team 1 → 0
v69h RECODE: Audi Q8 > Lexus NX — evidence test_drove_both → opinion
zt5h RECODE: Range Rover > Lexus RX — evidence owned_one_td_other → opinion_plus_drive [model not named — thread inference]
v2n5 DELETE: Range Rover > Mercedes GLE — remove row
b3qj DELETE: Range Rover > BMW X5 — remove row
gj8c RECODE: Lexus ES > Lexus RX — evidence owned_both → test_drove_both
z4zt RECODE: Genesis GV80 > Lincoln Navigator — evidence test_drove_both → opinion
bq6e QUOTE_FIX: Lincoln Navigator > Hyundai Palisade — replace quote with: "…My wife loves her '23 Palisade and she has owned a laundry list of luxury/premium brand SUV's before it. I've been surprised with it as well in terms of ride and comfort, particularly for the cost, but I wouldn't put it anywhere near the top of the charts. I have an Escalade in the biz fleet that's very comfortable all around but I think the newest Navigator is probably better."
bq6e RECODE: Lincoln Navigator > Hyundai Palisade — evidence owned_one_td_other → opinion_plus_drive
ef6z QUOTE_FIX: Cadillac Escalade > Hyundai Palisade — replace quote with: "…My wife loves her '23 Palisade and she has owned a laundry list of luxury/premium brand SUV's before it. I've been surprised with it as well in terms of ride and comfort, particularly for the cost, but I wouldn't put it anywhere near the top of the charts. I have an Escalade in the biz fleet that's very comfortable all around but I think the newest Navigator is probably better."
mp7z DELETE: Range Rover > Hyundai Palisade — remove row
zj2w OK: Lexus LX > Genesis GV80 — keep as-is; fuller quote suggested: "I replaced my 2013 Lexus at 300K miles with a new LX after driving everything else in the price range. I will say the Genesis GV was close 2nd overall in my comparisons in comfort/driver features/ride/cabin noise, but was a bit too small… Mercedes GLS was my size equivalent 2nd choice and matches the Lexus pretty well. But the Lexus with the adaptive suspension is just a very pleasant car to own."
rjy3 OK: Lexus LX > Mercedes GLS — keep as-is; fuller quote suggested: "I replaced my 2013 Lexus at 300K miles with a new LX after driving everything else in the price range. I will say the Genesis GV was close 2nd overall in my comparisons in comfort/driver features/ride/cabin noise, but was a bit too small… Mercedes GLS was my size equivalent 2nd choice and matches the Lexus pretty well. But the Lexus with the adaptive suspension is just a very pleasant car to own."
g3ta OK: Range Rover > Range Rover Sport — keep as-is
wha2 QUOTE_FIX: Range Rover Sport > Mercedes GLE — replace quote with: "…of all the vehicles my wife and I have owned… the GLE was perhaps the poorest handling of them all… I hated how it drove. … What's nice is that I never felt tired after a long trip from Vegas to L.A. and back."
qj5r OK: Range Rover Sport > Porsche Cayenne — keep as-is
syb3 QUOTE_FIX: Range Rover Sport > BMW X5 — replace quote with: "I test drove a Cayenne, X5 and a RRS. Porsche felt sporty, Range Rover felt like sitting on a cloud and more luxury. … I chose my RRS."
cj4j OK: Range Rover Sport > Porsche Cayenne — keep as-is
h893 RECODE: Range Rover Sport > Mercedes GLE — evidence test_drove_both → opinion_plus_drive
df4x OK: Range Rover > Audi Q8 — keep as-is
ux87 OK: Range Rover Sport > Volvo XC90 — keep as-is; fuller quote suggested: "Before we briefly had an XC90 T8 Recharge. I didn't really like the Volvo that much: It was quite 'boaty' (swaying left and right in turns and up and down when accelerating and breaking)… the Range Rover in my opinion looks better and the driving feel is almost incomparable."
mh6d OK: Tesla Model X > Tesla Model Y — keep as-is
jf27 RECODE: Hyundai Palisade > Tesla Model Y — evidence owned_one_td_other → opinion
bbb7 OK: Hyundai Palisade > Kia Telluride — keep as-is
bbb7 RECODE: Hyundai Palisade > Kia Telluride — home_team 0 → 1
zhy4 RECODE: Hyundai Palisade > Kia Telluride — evidence test_drove_both → owned_one_td_other
zhy4 RECODE: Hyundai Palisade > Kia Telluride — home_team 0 → 1
yb8z OK: Kia Telluride > Hyundai Palisade — keep as-is
ah3s RECODE: Land Rover > Volvo XC60 — evidence test_drove_both → opinion_plus_drive
ah3s QUOTE_FIX: Land Rover > Volvo XC60 — replace quote with: "When I test drove the XC60 i think it either had 20" wheels or run flats because it rode like shit. … For comfort the only answer is a Land Rover product (includes Range Rover). You have to sacrifice on reliability but they have air suspension / cushy seats figured out."
ph39 OK: Volvo XC60 > BMW X1 — keep as-is
qk7v RECODE: Audi Q5 > BMW X3 — evidence owned_one_td_other → opinion
z3kt QUOTE_FIX: Volvo XC60 > BMW X3 — replace quote with: "Volvo is great, with a bit of a soft ride. BMW x3 is more on the firm side."
z3kt RECODE: Volvo XC60 > BMW X3 — evidence owned_one_td_other → opinion
qun7 DELETE: Toyota Highlander > Honda CR-V — remove row
vpr5 DELETE: Mazda CX-9 > Mazda CX-50 — remove row
md9d DELETE: Acura MDX > Lexus RX — remove row
f6gj OK: Genesis GV80 > Mercedes GLE — keep as-is
gq32 OK: Genesis GV80 > BMW X5 — keep as-is
y9hf OK: BMW X5 > Mercedes GLE — keep as-is; fuller quote suggested: "GLE feels heavier, like driving a pontoon boat. The X5 feels like a ski boat. Light, nimble, like its gliding along the road… Overall I enjoy the X5 so much better than the MB, mainly because of the ride and smooth acceleration."
b7bb OK: Range Rover Sport > Mercedes GLE AMG — keep as-is
b7bb RECODE: Range Rover Sport > Mercedes GLE AMG — home_team 0 → 1
pa49 QUOTE_FIX: BMW iX > Tesla Model X — replace quote with: "The new BMW iX handles better than the Tesla Model X. The new BMW iX is more refined than the Model X. The new BMW iX is more comfortable than the Model X."
f89w OK: Hyundai Palisade > Mazda CX-90 — keep as-is
f48w RECODE: Hyundai Palisade > Toyota Grand Highlander — evidence test_drove_both → opinion_plus_drive
e3xv RECODE: Lexus TX > Toyota Grand Highlander — evidence test_drove_both → opinion
j33d OK: Hyundai Palisade > Toyota Highlander — keep as-is
xe8m OK: Toyota Highlander > Hyundai Palisade — keep as-is
eqj9 OK: Toyota Highlander > Honda Pilot — keep as-is [model not named — thread inference]
k5hb OK: Toyota Grand Highlander > Hyundai Palisade — keep as-is
gd2f OK: Hyundai Palisade > Toyota Grand Highlander — keep as-is
f84v RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → opinion
sv5y OK: Hyundai Palisade > Honda Pilot — keep as-is
v9jt RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → opinion_plus_drive
v9jt QUOTE_FIX: Hyundai Palisade > Honda Pilot — add parent/thread context: "Palisade vs Pilot"
rt6d RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → opinion_plus_drive
rt6d QUOTE_FIX: Hyundai Palisade > Honda Pilot — add parent/thread context: "Palisade vs Pilot"
p6ng OK: Hyundai Palisade > Kia Telluride — keep as-is
rx8s OK: Hyundai Palisade > Toyota Highlander — keep as-is
y3dc OK: Hyundai Palisade > Kia Telluride — keep as-is
wu48 DELETE: Hyundai Palisade > Lexus TX — remove row
pq3c DELETE: Hyundai Palisade > Toyota Grand Highlander — remove row
c735 OK: Hyundai Palisade > Toyota Highlander — keep as-is
u99j OK: Lincoln Aviator > BMW X5 — keep as-is
me2m QUOTE_FIX: Lincoln Aviator > BMW X5 — replace quote with: "I have a 2025 X5 and a 2026 Aviator..... My personal favorite of the 2 is the Aviator but I love the X5 as well. Both feel very premium… the Aviator is smoother. The BMW is quicker but the Aviator is more powerful…"
cxx9 OK: BMW X5 > Lincoln Aviator — keep as-is
dug9 OK: BMW X7 > Lincoln Aviator — keep as-is
n2qd OK: Lincoln Aviator > BMW X7 — keep as-is
n2qd RECODE: Lincoln Aviator > BMW X7 — home_team 0 → 1
u6eq OK: Lincoln Aviator > Lexus TX — keep as-is
u6eq RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
u4r3 OK: Mercedes GLS > BMW X7 — keep as-is
m5ju OK: Mercedes GLS > BMW X7 — keep as-is
b5ed OK: Mercedes GLS > BMW X7 — keep as-is
zw59 OK: Mercedes GLS > BMW X7 — keep as-is
de98 RECODE: Cadillac Escalade > BMW X7 — evidence opinion_plus_drive → opinion
jg8n OK: BMW X7 > Cadillac Escalade — keep as-is
jg8n QUOTE_FIX: BMW X7 > Cadillac Escalade — replace quote with: "…the kids are actually a bit more comfortable in the second row than the Caddy… I find it to ride smoother than the Caddy."
a6aj OK: Tesla Model X > Cadillac Escalade — keep as-is
a6aj RECODE: Tesla Model X > Cadillac Escalade — home_team 0 → 1
ea5z OK: Cadillac Escalade > Tesla Model X — keep as-is
zy3a OK: Cadillac Escalade > Tesla Model X — keep as-is
n8hq OK: Lincoln Nautilus > Lexus RX — keep as-is [model not named — thread inference]
fm3z OK: Volvo XC60 > Lincoln Nautilus — keep as-is [model not named — thread inference]
fm3z RECODE: Volvo XC60 > Lincoln Nautilus — home_team 0 → 1
ex8t OK: Lincoln Nautilus > Volvo XC60 — keep as-is [model not named — thread inference]
gkv4 RECODE: Audi Q7 > Volvo XC90 — evidence test_drove_both → opinion
qy8s RECODE: Volvo XC90 > Audi Q7 — evidence test_drove_both → opinion
wwj2 OK: Audi Q7 > Volvo XC90 — keep as-is
kam6 OK: Audi Q7 > Volvo XC90 — keep as-is
kam6 RECODE: Audi Q7 > Volvo XC90 — home_team 0 → 1
ebe6 OK: Hyundai Palisade > Lincoln Nautilus — keep as-is
p2m4 OK: Hyundai Palisade > Lincoln Aviator — keep as-is
by4e OK: Hyundai Palisade > Ford Explorer — keep as-is
k9xq OK: Hyundai Palisade > Honda Pilot — keep as-is
dh9m OK: Ford Explorer > Kia Telluride — keep as-is
dn5c OK: Kia Telluride > Honda Pilot — keep as-is
ww5n OK: Lincoln Navigator > Cadillac Escalade — keep as-is
b6dn OK: Cadillac Escalade > Lincoln Navigator — keep as-is
b2w2 DELETE: Mercedes GLS > Lincoln Navigator — remove row
xm8t OK: Toyota Highlander > Toyota RAV4 — keep as-is
gd5g OK: Honda CR-V > Toyota RAV4 — keep as-is
j8ge QUOTE_FIX: Hyundai Palisade > Toyota Highlander — replace quote with: "I owned a 2020 palisade platinum and a 2023 highlighter platinum. The Palisade ride is alot smoother"
k8ss OK: Hyundai Palisade > Honda Pilot — keep as-is
e3mt RECODE: Honda Pilot > Hyundai Palisade — evidence test_drove_both → opinion_plus_drive
e3mt RECODE: Honda Pilot > Hyundai Palisade — home_team 0 → 1
bw88 OK: Hyundai Palisade > Toyota Highlander — keep as-is [model not named — thread inference]
bw88 RECODE: Hyundai Palisade > Toyota Highlander — home_team 0 → 1
tfm5 OK: Hyundai Palisade > Honda Pilot — keep as-is [model not named — thread inference]
tfm5 RECODE: Hyundai Palisade > Honda Pilot — home_team 0 → 1
qvw3 RECODE: Hyundai Palisade > Volkswagen Atlas — evidence test_drove_both → opinion_plus_drive
qvw3 RECODE: Hyundai Palisade > Volkswagen Atlas — home_team 0 → 1
f3xe OK: Hyundai Palisade > Honda Pilot — keep as-is
f3xe RECODE: Hyundai Palisade > Honda Pilot — home_team 0 → 1
pf8r OK: Hyundai Palisade > Kia Telluride — keep as-is
z799 OK: Hyundai Palisade > Toyota Highlander — keep as-is
r6sq DELETE: Hyundai Palisade > Toyota Grand Highlander — remove row
j5zb OK: Hyundai Palisade > Mazda CX-90 — keep as-is [model not named — thread inference]
j5zb RECODE: Hyundai Palisade > Mazda CX-90 — home_team 0 → 1
psj5 RECODE: Mazda CX-90 > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
psj5 RECODE: Mazda CX-90 > Hyundai Palisade — home_team 0 → 1
v288 OK: Hyundai Palisade > Toyota Grand Highlander — keep as-is [model not named — thread inference]
v288 RECODE: Hyundai Palisade > Toyota Grand Highlander — home_team 0 → 1
db3r RECODE: Toyota Grand Highlander > Hyundai Palisade — evidence test_drove_both → opinion
b78a OK: Hyundai Palisade > Subaru Ascent — keep as-is
b78a RECODE: Hyundai Palisade > Subaru Ascent — home_team 0 → 1
d52d OK: Subaru Ascent > Hyundai Palisade — keep as-is [model not named — thread inference]
d52d RECODE: Subaru Ascent > Hyundai Palisade — home_team 0 → 1
jh9f OK: Hyundai Palisade > Toyota Highlander — keep as-is
rhy3 OK: Hyundai Palisade > Honda Pilot — keep as-is
fb37 OK: Subaru Ascent > Hyundai Palisade — keep as-is [model not named — thread inference]
uze8 OK: Subaru Ascent > Kia Telluride — keep as-is [model not named — thread inference]
f2db OK: Subaru Ascent > Toyota Grand Highlander — keep as-is [model not named — thread inference]
u2bm OK: Kia Telluride > Ford Explorer — keep as-is
u2bm RECODE: Kia Telluride > Ford Explorer — home_team 0 → 1
h9nk OK: Kia Telluride > Toyota Highlander — keep as-is
h9nk RECODE: Kia Telluride > Toyota Highlander — home_team 0 → 1
z4xg OK: Honda Pilot > Toyota Highlander — keep as-is
z4xg RECODE: Honda Pilot > Toyota Highlander — home_team 0 → 1
mu9d OK: Toyota Grand Highlander > Hyundai Palisade — keep as-is
mu9d RECODE: Toyota Grand Highlander > Hyundai Palisade — home_team 0 → 1
k35x OK: Toyota Grand Highlander > Kia Telluride — keep as-is
k35x RECODE: Toyota Grand Highlander > Kia Telluride — home_team 0 → 1
zwx4 OK: Lincoln Aviator > Volvo XC90 — keep as-is
hew3 OK: Lincoln Aviator > BMW X5 — keep as-is
xg5y OK: Cadillac Escalade > Lincoln Navigator — keep as-is
y2rj OK: Cadillac Escalade > Lincoln Navigator — keep as-is [model not named — thread inference]
y2rj RECODE: Cadillac Escalade > Lincoln Navigator — home_team 1 → 0
gn5g OK: Lincoln Navigator > Cadillac Escalade — keep as-is
w93g OK: Cadillac Escalade > Lincoln Navigator — keep as-is [model not named — thread inference]
j2hx OK: Lincoln Navigator > Cadillac Escalade — keep as-is
kf2m OK: Audi Q7 > BMW X5 — keep as-is
mv2v OK: Audi Q7 > BMW X5 — keep as-is
j6rv OK: Audi Q8 > Audi Q7 — keep as-is
u2sr QUOTE_FIX: BMW X5 > Acura MDX — replace quote with: "For the suspension, I'd say it was like the MDX but more refined. It handled imperfections much better"
s6ea OK: Acura MDX > Audi Q7 — keep as-is
y4ae RECODE: Acura MDX > BMW X5 — evidence owned_both → test_drove_both [model not named — thread inference]
kb6j OK: BMW X5 > Lexus GX — keep as-is
fwk6 OK: BMW X7 > Lexus GX — keep as-is
e6ak OK: Lincoln Nautilus > Lexus RX — keep as-is
cp26 OK: Genesis GV80 > BMW X5 — keep as-is
t8kb QUOTE_FIX: Genesis GV70 > Audi Q5 — replace quote with: "GV70 was most comfortable by a decent margin with the Volvo in second"
f8eq OK: Porsche Cayenne > BMW X5 — keep as-is
k36j OK: Mercedes GLC > BMW X3 — keep as-is
p42w QUOTE_FIX: Mercedes GLC > BMW X3 — replace quote with: "the Mercedes was FAR more comfortable for us… you get more comfort snd quiet with Mercedes"
p42w RECODE: Mercedes GLC > BMW X3 — evidence test_drove_both → owned_one_td_other
r7an QUOTE_FIX: Acura MDX > Volvo XC90 — replace quote with: "I own a 2016 xc90… and 2022 MDX tech… MDX smoother ride, absorbs bumps better, feels larger than xc90…"
j6v6 OK: Lexus RX > BMW X5 — keep as-is
j8fr OK: Genesis GV70 > Volvo XC60 — keep as-is
f74u OK: Lexus RX > Volvo XC60 — keep as-is
y2t3 RECODE: Honda Pilot > Kia Telluride — evidence test_drove_both → owned_one_td_other
g65r QUOTE_FIX: Toyota Highlander > Toyota Venza — replace quote with: "The Venza was too small, rides a bit stiff and road noise was irritating… It's a solid vehicle, feels much more substantial and drives much smoother than the Venza"
j4qc OK: Toyota Venza > Toyota Highlander — keep as-is
d6bv OK: Hyundai Palisade > Honda CR-V — keep as-is
jh5a RECODE: Hyundai Palisade > Kia Telluride — evidence owned_both → owned_one_td_other
nfa8 OK: Subaru Outback > Honda CR-V — keep as-is
jmc7 OK: Mazda CX-5 > Toyota RAV4 — keep as-is
t9v3 OK: Honda CR-V > Mazda CX-50 — keep as-is
bv7d QUOTE_FIX: Mazda CX-5 > Mazda CX-50 — replace quote with: "The driver seat is the most uncomfortable seat I have ever sat in. Total miss from the cx5"
bv7d RECODE: Mazda CX-5 > Mazda CX-50 — evidence owned_both → opinion
dyv3 OK: Honda Pilot > Honda CR-V — keep as-is
h7uq OK: Lincoln Aviator > Lexus RX — keep as-is
u2n5 OK: Lexus NX > Lexus RX — keep as-is
be9j OK: Subaru Outback > Toyota RAV4 — keep as-is
fw8v RECODE: Subaru Outback > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
my28 OK: Subaru Outback > Subaru Forester — keep as-is
my28 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
ajk8 OK: Subaru Outback > Subaru Crosstrek — keep as-is
ajk8 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
bz6a OK: Honda CR-V > Subaru Outback — keep as-is
vs35 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
nv9p QUOTE_FIX: Subaru Outback 2026 > Subaru Forester — replace quote with: "To be fair, it is nicer in a lot of ways — quieter cabin, smoother ride… but I couldn't get past the driving position and sightlines"
nv9p RECODE: Subaru Outback 2026 > Subaru Forester — evidence test_drove_both → owned_one_td_other
mkk3 OK: Subaru Outback 2026 > Toyota 4Runner — keep as-is [model not named — thread inference]
yy48 OK: Subaru Ascent > Hyundai Palisade — keep as-is
d5v8 OK: Subaru Ascent > Kia Telluride — keep as-is
w3qy OK: Subaru Ascent > Toyota Highlander — keep as-is
e8w7 OK: Kia Telluride > Subaru Ascent — keep as-is
s8b2 RECODE: Subaru Ascent > Kia Telluride — evidence test_drove_both → owned_one_td_other
bz7g RECODE: Subaru Ascent > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
bge2 RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
fdq6 QUOTE_FIX: Subaru Ascent > Subaru Outback — replace quote with: "We test drove all 3 and at 70mph the Ascent was roughly 5dB quieter than both. Suspension is softest, more comfortable on bad Michigan roads"
fdq6 RECODE: Subaru Ascent > Subaru Outback — evidence test_drove_both → owned_one_td_other
jpe7 QUOTE_FIX: Subaru Ascent > Subaru Forester — replace quote with: "We test drove all 3 and at 70mph the Ascent was roughly 5dB quieter than both"
jpe7 RECODE: Subaru Ascent > Subaru Forester — evidence test_drove_both → owned_one_td_other
w98d OK: Subaru Ascent > Chevrolet Suburban — keep as-is [model not named — thread inference]
n8jg OK: Lexus RX > Lexus GX — keep as-is
n8jg RECODE: Lexus RX > Lexus GX — home_team 0 → 1
umh9 QUOTE_FIX: Lexus GX > Lexus RX — replace quote with: "I had the 2021 RX 350 and now the 2023 GX 460… I enjoy the ride of the GX 460 better. I think that the ride is smoother"
umh9 RECODE: Lexus GX > Lexus RX — home_team 0 → 1
x6cm OK: Lexus RX > Toyota Highlander — keep as-is
x6cm RECODE: Lexus RX > Toyota Highlander — home_team 0 → 1
h6cb RECODE: Lexus GX > Toyota 4Runner — evidence test_drove_both → owned_one_td_other [model not named — thread inference]
gk4e OK: Lexus GX > Toyota 4Runner — keep as-is
q8ns OK: Lexus GX > Toyota 4Runner — keep as-is
h62w OK: Subaru Outback > Toyota RAV4 — keep as-is
wxs2 OK: Subaru Outback > Toyota RAV4 — keep as-is
g5s4 OK: Subaru Outback > Toyota RAV4 — keep as-is
xq8p RECODE: Subaru Outback > Subaru Forester — evidence owned_both → opinion_plus_drive
xq8p RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
veg4 OK: Subaru Outback > Subaru Forester — keep as-is
veg4 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
hv8g OK: Subaru Outback > Subaru Forester — keep as-is
hv8g RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
qz7v OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
rn7y RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
jg5g OK: Subaru Ascent > Subaru Outback — keep as-is
nya2 OK: Subaru Ascent > Subaru Forester — keep as-is
mgu3 OK: Lexus RX > Lexus GX — keep as-is
mgu3 RECODE: Lexus RX > Lexus GX — home_team 0 → 1
j6sb OK: Lexus GX > Lexus RX — keep as-is
j6sb RECODE: Lexus GX > Lexus RX — home_team 0 → 1
q7fw QUOTE_FIX: Lexus GX > Lexus RX — replace quote with: "I own a GX… driven an RX loaner… less wind/road noise"
q7fw RECODE: Lexus GX > Lexus RX — home_team 0 → 1
qw7d OK: Lexus RX > Lexus GX — keep as-is
qw7d RECODE: Lexus RX > Lexus GX — home_team 0 → 1
h8zg QUOTE_FIX: Lexus RX > Toyota Highlander — replace quote with: "We made the trade… it is such a smoother ride. Quieter cabin, smooth V6, so comfortable"
h8zg RECODE: Lexus RX > Toyota Highlander — home_team 0 → 1
nuc4 OK: Lexus GX > Toyota 4Runner — keep as-is
eh4x OK: Lexus GX > Toyota 4Runner — keep as-is
u6kk OK: Lexus GX > Toyota 4Runner — keep as-is
adm3 OK: Lexus GX > Toyota 4Runner — keep as-is
s4fc OK: Subaru Outback > Honda CR-V — keep as-is
gx2m OK: Subaru Outback > Honda CR-V — keep as-is [model not named — thread inference]
jah5 QUOTE_FIX: Subaru Outback > Honda CR-V — replace quote with: "I have both. A 2024 crv sport touring (hybrid) and a 2025 outback touring XT… for me the outback wins in comfort - both as driver and passenger… after driving the Outback for a few months, it now seems noisier to me"
xxx8 OK: Honda CR-V > Subaru Outback — keep as-is
xxx8 RECODE: Honda CR-V > Subaru Outback — home_team 1 → 0
g5nz OK: Subaru Outback > Honda CR-V — keep as-is
vtk5 OK: Honda CR-V > Subaru Outback — keep as-is
u3wz OK: Honda CR-V > Subaru Outback — keep as-is
ctz4 QUOTE_FIX: Mazda CX-5 > Subaru Outback — replace quote with: "Test of very low miles CX-5… Very quiet. Little road noise… 2024 Outback demo… Suspension was just harsh… Lots of road noise, lots of suspension noise"
usy5 OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
dg4t OK: Subaru Outback 2026 > Subaru Outback — keep as-is [model not named — thread inference]
q52t OK: Honda CR-V > Subaru Outback 2026 — keep as-is
q52t RECODE: Honda CR-V > Subaru Outback 2026 — home_team 1 → 0
rv9d QUOTE_FIX: Subaru Outback 2026 > Honda CR-V — replace quote with: "The driver seat was okay… not as lounge comforting as the OB… Sitting drivers in the OB was just very comfortable"
w9tj OK: Subaru Outback 2026 > Subaru Ascent — keep as-is [model not named — thread inference]
r7ze OK: Subaru Outback 2026 > Toyota RAV4 — keep as-is [model not named — thread inference]
v6pk OK: Hyundai Palisade > Subaru Ascent — keep as-is
r6ac OK: Subaru Ascent > Hyundai Palisade — keep as-is
hhm9 OK: Honda Pilot > Subaru Ascent — keep as-is
nf63 OK: Honda Pilot > Subaru Ascent — keep as-is
u5ad OK: Subaru Outback > Subaru Ascent — keep as-is
sm4u OK: Subaru Outback > Subaru Ascent — keep as-is
k6hs OK: Subaru Ascent > Subaru Outback — keep as-is
qrj5 OK: Subaru Ascent > Subaru Outback — keep as-is
vgd3 RECODE: Subaru Ascent > Volkswagen Atlas — evidence test_drove_both → owned_one_td_other
k5dc RECODE: Subaru Ascent > Toyota Highlander — evidence test_drove_both → owned_one_td_other
w2kc RECODE: Subaru Ascent > Honda Pilot — evidence test_drove_both → owned_one_td_other
w5mc OK: Hyundai Palisade > Subaru Ascent — keep as-is [model not named — thread inference]
y7uj OK: Lexus RX > Toyota RAV4 — keep as-is
b669 QUOTE_FIX: Lexus RX > Audi Q5 — replace quote with: "I traded my 2016 Audi Q5 Premium Plus for the RX350 Premium AWD… Very comfortable and roomy… Seating in the Audi Q5 was very tight"
kse9 QUOTE_FIX: Volvo XC90 > Lexus RX — replace quote with: "I was so disappointed with the RX. Test drove against the cx-9, MDX, xc90, gle350, q7, and x5. Easily the most jarring ride"
zv7u OK: Lexus RX > Lexus GX — keep as-is
zv7u RECODE: Lexus RX > Lexus GX — home_team 0 → 1
kb5w QUOTE_FIX: Lexus RX > Lexus GX — replace quote with: "I moved from RX to GX. Ride is definitely day and night difference. You'll probably notice that coming from BMW X5. But again GX is a truck body on frame."
j5fn OK: Lexus GX > Lexus RX — keep as-is
ad9z OK: Lexus GX > Lexus TX — keep as-is
pdc2 OK: Lexus TX > Lexus GX — keep as-is
pdc2 RECODE: Lexus TX > Lexus GX — home_team 0 → 1
f2gm OK: Lexus LX > Lexus GX — keep as-is
eng3 OK: Lexus LX > Lexus GX — keep as-is [model not named — thread inference]
pr7y OK: Lexus GX > Toyota 4Runner — keep as-is
pt8e RECODE: Lexus GX > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
m2qn OK: Lexus GX > Lexus GX 550 — keep as-is [model not named — thread inference]
nb6f QUOTE_FIX: Lexus RX > Audi Q7 — replace quote with: "Ride quality is meh compared to RX350L or at least imo. Even the 55"
nb6f RECODE: Lexus RX > Audi Q7 — evidence test_drove_both → opinion
adz9 OK: Lexus NX > Mercedes GLC — keep as-is
qc7t OK: Lexus NX > Mercedes GLC — keep as-is
kjh8 OK: Lincoln Corsair > BMW X3 — keep as-is
gnc2 OK: Lincoln Nautilus > BMW X3 — keep as-is
n5yv OK: GV70 > Macan — keep as-is
fae7 OK: GV70 > Q5 — keep as-is
hpv2 OK: GV70 > BMW X3 — keep as-is
d8z9 OK: Macan > BMW X3 — keep as-is
zr3r OK: Q5 > BMW X3 — keep as-is
r4gx OK: GV70 > Porsche Macan — keep as-is
j4vz OK: GV70 > Audi Q5 — keep as-is
dt3x OK: Lincoln Nautilus > Lexus RX — keep as-is
npd7 OK: Toyota Venza > Honda CR-V — keep as-is
bff5 QUOTE_FIX: Toyota Venza > Honda CR-V — replace quote with: "My Venza is like a baby Lexus on the inside. The seat comfort is PHENOMENAL and the main reason I bought the car. I have to haul a lot of equipment and move large boxes with my job, so I miss the cargo practicality of my CR-V."
c77w RECODE: Honda CR-V > Toyota Venza — evidence test_drove_both → owned_one_td_other
qv58 OK: Volvo XC60 > Lexus NX — keep as-is
q22k RECODE: Volvo XC60 > Lexus NX — evidence test_drove_both → owned_one_td_other
c4qe OK: Volvo XC60 > Lexus NX — keep as-is
ag2p RECODE: Lexus NX > Volvo XC60 — evidence test_drove_both → owned_one_td_other
fza5 OK: Volvo XC60 > Porsche Macan — keep as-is [model not named — thread inference]
uc8s OK: Honda CR-V > Mazda CX-50 — keep as-is
fgb5 OK: Mazda CX-5 > Mazda CX-50 — keep as-is
w46q OK: Honda CR-V > Mazda CX-50 — keep as-is
g9wa RECODE: Honda CR-V > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
vvy3 RECODE: Honda CR-V > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
d27v OK: Honda CR-V > Mazda CX-50 — keep as-is
kk39 RECODE: Honda CR-V > Mazda CX-50 — evidence test_drove_both → owned_one_td_other
u94u OK: Honda CR-V > Mazda CX-5 — keep as-is [model not named — thread inference]
c244 OK: Volvo XC60 > Audi Q5 — keep as-is
rz88 OK: Audi Q5 > Mercedes GLC — keep as-is
fq49 RECODE: Lincoln Nautilus > Cadillac XT5 — evidence test_drove_both → owned_one_td_other
te3q OK: Lincoln Nautilus > Cadillac XT5 — keep as-is
e8k5 OK: Honda CR-V > Volkswagen Tiguan — keep as-is
m4bd RECODE: Honda CR-V > Volkswagen Tiguan — evidence test_drove_both → owned_one_td_other
bbd4 OK: Audi Q5 > Lexus NX — keep as-is
u9a8 OK: Genesis GV70 > BMW X3 — keep as-is [model not named — thread inference]
se8k RECODE: Genesis GV70 > BMW X3 — evidence test_drove_both → owned_one_td_other
v5kd OK: Mercedes GLE > Volvo XC90 — keep as-is [model not named — thread inference]
uat7 OK: Mercedes GLE > Audi Q7 — keep as-is [model not named — thread inference]
p8rx RECODE: Audi Q7 > BMW X5 — evidence test_drove_both → owned_one_td_other
qx6q RECODE: Audi Q7 > Mercedes GLE — evidence test_drove_both → owned_one_td_other
x2ez RECODE: Lincoln Aviator > Genesis GV80 — evidence test_drove_both → owned_one_td_other
kae6 RECODE: Lincoln Aviator > Genesis GV80 — evidence test_drove_both → owned_one_td_other
rw8x RECODE: Acura MDX > Genesis GV80 — evidence test_drove_both → owned_one_td_other
bn4y OK: Mercedes GLE > Porsche Cayenne — keep as-is
s77b OK: BMW X5 > Tesla Model X — keep as-is
p7t4 OK: BMW iX > Tesla Model X — keep as-is
x3m9 OK: BMW iX > Tesla Model X — keep as-is
dt7g QUOTE_FIX: BMW iX > Tesla Model X — replace quote with: "DRIVE QUALITY/ROAD NOISE —> all caps because it's not remotely close; you can barely have a conversation on the highway in the X"
gms9 OK: BMW iX > Tesla Model X — keep as-is
f3df OK: Acura MDX > BMW X5 — keep as-is
xyu3 OK: Acura MDX > BMW X5 — keep as-is
a3c8 OK: BMW X5 > Acura MDX — keep as-is
tn9p RECODE: Lexus TX > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
g35e OK: Lincoln Aviator > Volvo XC90 — keep as-is
uw6h RECODE: BMW iX > Mercedes EQS SUV — evidence test_drove_both → owned_one_td_other
bx2a OK: BMW iX > BMW X5 — keep as-is
t8k5 OK: BMW iX > BMW X5 — keep as-is
w26x RECODE: BMW iX > BMW X5 — evidence owned_one_loaner → owned_both
mb76 RECODE: BMW X5 > BMW iX — evidence test_drove_both → owned_one_td_other
j4h2 OK: BMW X5 > Tesla Model Y — keep as-is
g9f4 OK: BMW X5 > Tesla Model Y — keep as-is
h6vg OK: Audi Q8 > Genesis GV80 — keep as-is
ar5q OK: Acura MDX > Genesis GV80 — keep as-is
c6tz OK: Kia Telluride > Nissan Pathfinder — keep as-is
s5w3 OK: Nissan Pathfinder > Honda Pilot — keep as-is
zu87 RECODE: Nissan Pathfinder > Honda Passport — evidence test_drove_both → owned_one_td_other
j726 RECODE: Nissan Pathfinder > Honda Pilot — evidence test_drove_both → owned_one_td_other
p2yk OK: Nissan Pathfinder > Honda Pilot — keep as-is
w34z OK: Nissan Pathfinder > Honda Pilot — keep as-is
sp4v OK: Nissan Pathfinder > Honda Pilot — keep as-is
f5sz RECODE: Nissan Pathfinder > Honda Pilot — evidence test_drove_both → owned_one_td_other
bv24 OK: Kia Telluride > Kia Sorento — keep as-is
k3up OK: Kia Telluride > Kia Sorento — keep as-is [model not named — thread inference]
a4px RECODE: Kia Telluride > Kia Sorento — evidence test_drove_both → owned_one_td_other
bzz7 OK: Honda Passport > Honda Pilot — keep as-is
u3yf RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
kaq3 RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
nyr4 RECODE: Volkswagen Atlas > Honda Pilot — evidence test_drove_both → owned_one_td_other
s3ma OK: Volkswagen Atlas > Honda Pilot — keep as-is
fq7n OK: Honda Pilot > Kia Telluride — keep as-is
c9z5 OK: Kia Telluride > Honda Pilot — keep as-is
a7un OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
dnp2 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
m8x9 RECODE: Kia Telluride > Volkswagen Atlas — evidence owned_one_td_other → test_drove_both
y4xv OK: Volkswagen Atlas > Kia Telluride — keep as-is
n8zp OK: Hyundai Palisade > Nissan Pathfinder — keep as-is
v2jb RECODE: Hyundai Palisade > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
qt8w OK: Hyundai Palisade > Nissan Pathfinder — keep as-is
fd7b RECODE: Hyundai Palisade > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
m4af OK: Kia Telluride > Ford Explorer — keep as-is [model not named — thread inference]
pp54 QUOTE_FIX: Kia Telluride > Ford Explorer — replace quote with: "I had a 2017 Explorer, and it drove bulky like a truck… It handles like a car"
x2u9 OK: Kia Telluride > Ford Explorer — keep as-is
gf5x OK: Honda Pilot > Honda Passport — keep as-is
d6yg OK: Honda Pilot > Honda Passport — keep as-is
ta24 RECODE: Honda Pilot > Honda Passport — evidence test_drove_both → owned_one_td_other
x8j2 QUOTE_FIX: Honda Passport > Honda Pilot — replace quote with: "the seats are very uncomfortable… I loved the comfort of the seat"
x8j2 RECODE: Honda Passport > Honda Pilot — evidence test_drove_both → owned_one_td_other
m7gb RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
t4g2 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
kxf3 QUOTE_FIX: Honda Pilot > Toyota Grand Highlander — replace quote with: "We thought the GH was like driving a boat and I've seen some say they've gotten carsick either driving or riding in the GH."
kxf3 RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
q9bv OK: Honda Pilot > Volkswagen Atlas — keep as-is
e7ta RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
w5tr RECODE: Honda Pilot > Toyota Highlander — evidence test_drove_both → owned_one_td_other
y2cg RECODE: Honda Pilot > Kia Telluride — evidence test_drove_both → owned_one_td_other
rjx8 OK: Nissan Pathfinder > Honda Pilot — keep as-is
xx3e OK: Nissan Pathfinder > Toyota Highlander — keep as-is
n4gg QUOTE_FIX: Kia Telluride > Honda Pilot — replace quote with: "Honda Pilot - Elite - … smooth ride but feels somewhat like driving a vehicle with a truck frame … KIA - Telluride - … drives like a car, great visibility"
ea57 QUOTE_FIX: Kia Telluride > Jeep Grand Cherokee L — replace quote with: "Jeep Grand Cherokee L - Limited - Drives like a truck; it is on a RAM 1500 frame … KIA - Telluride - … drives like a car, great visibility"
hy4u OK: Mercedes GLS > BMW X7 — keep as-is
djc7 OK: Mercedes GLS > BMW X7 — keep as-is
vu5k QUOTE_FIX: Mercedes GLS > BMW X7 — replace quote with: "I have a sister who has a gls 450 and one that has an x7 40i. I like the x7 much better. I've driven both, the x7 seems a lot tighter while driving. The Mercedes is a lot more plush and is a bit bigger."
vds6 OK: Mercedes GLS > BMW X5 — keep as-is
u8uv RECODE: Range Rover > BMW X7 — evidence test_drove_both → owned_one_td_other
p674 OK: Range Rover > BMW X7 — keep as-is [model not named — thread inference]
fm4v OK: BMW X7 > Range Rover — keep as-is
yba9 OK: Jeep Grand Wagoneer > Lincoln Navigator — keep as-is
yse2 OK: Lincoln Navigator > Jeep Grand Wagoneer — keep as-is
u7ez RECODE: Lincoln Navigator > Jeep Grand Wagoneer — evidence test_drove_both → owned_one_rode_other
m3xq RECODE: Lincoln Navigator > Jeep Grand Wagoneer — evidence owned_one_td_other → opinion_plus_drive
vhq4 RECODE: GMC Yukon > Jeep Grand Wagoneer — evidence owned_one_td_other → opinion_plus_drive
jyr6 OK: Jeep Grand Wagoneer > Chevrolet Suburban — keep as-is
tv5a OK: Jeep Grand Wagoneer > GMC Yukon — keep as-is
g266 RECODE: Jeep Grand Wagoneer > Chevrolet Suburban — evidence test_drove_both → opinion_plus_drive
j2q3 OK: Cadillac Escalade > Lincoln Navigator — keep as-is
v3fz OK: GMC Yukon > Lincoln Navigator — keep as-is [model not named — thread inference]
v3dc OK: Infiniti QX80 > Toyota Sequoia — keep as-is
p3ng QUOTE_FIX: Lexus GX 550 > Toyota 4Runner — replace quote with: "The seat position always created leg pain on longer trips… The comfort is amazing especially with the massage seats"
c9wv OK: Lexus GX 550 > Toyota 4Runner — keep as-is
b9ph OK: Lexus GX 550 > Toyota 4Runner — keep as-is [model not named — thread inference]
gm2p OK: Lexus GX 550 > Toyota 4Runner — keep as-is
g5e7 RECODE: Toyota 4Runner > Lexus GX 550 — evidence test_drove_both → owned_one_family
hgc2 RECODE: Lexus GX > Lexus GX 550 — evidence owned_one_rode_other → test_drove_both
jf77 QUOTE_FIX: Lexus GX 550 > Toyota Land Cruiser — replace quote with: "GX (Overtrail, I think) — Nice interior, quiet cabin… LandCruiser (Premium, whatever…the nice one) — Noiser than the GX… Tons of wind noise!!!"
gcu4 QUOTE_FIX: Lexus GX 550 > Toyota 4Runner — replace quote with: "4Runner (Limited and OR Premium) — Quieter than the LC, louder than the GX."
kz4s OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
gqp2 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
c426 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
wpg2 OK: GMC Yukon > Cadillac Escalade IQ — keep as-is
s66r OK: Lincoln Nautilus > Jeep Grand Cherokee — keep as-is
c8k7 RECODE: Mercedes GLC > Cadillac XT5 — evidence owned_one_td_other → opinion
b8xu OK: BMW X5 > Lexus RX — keep as-is
gk95 RECODE: Audi Q5 > BMW X3 — evidence owned_one_td_other → opinion
vdj2 QUOTE_FIX: Lincoln Navigator > Cadillac Escalade — replace quote with: "I moved from the Cadillac Escalade to the Lincoln Navigator and I am so happy I did. The seats are so amazingly comfortable… It drives so smooth and has so many wonderful features!"
qw4m OK: Audi Q5 > BMW X3 — keep as-is; SQ5 coded as Q5 (dataset convention)
p4hh OK: Mercedes GLE > Audi Q5 — keep as-is
ntw7 RECODE: Volvo XC60 > Mercedes GLC — evidence test_drove_both → owned_one_td_other
u7va RECODE: Mercedes GLE > BMW X5 — evidence test_drove_both → owned_one_td_other
q8s3 RECODE: Range Rover Sport > Mercedes GLE — loser Mercedes GLE → Mercedes GLE AMG
wz85 RECODE: Audi Q5 > Volvo XC60 — axis seats → overall
wz85 RECODE: Audi Q5 > Volvo XC60 — evidence test_drove_both → owned_one_td_other
n5cx RECODE: Audi Q5 > Mercedes GLC — axis seats → overall
n5cx RECODE: Audi Q5 > Mercedes GLC — evidence test_drove_both → owned_one_td_other
db82 RECODE: Audi Q5 > BMW X3 — axis seats → overall
db82 RECODE: Audi Q5 > BMW X3 — evidence test_drove_both → owned_one_td_other
euj3 OK: Cadillac XT6 > Acura MDX — keep as-is
uzy5 OK: Buick Enclave > Cadillac XT6 — keep as-is
pv5h OK: Volkswagen Atlas > Nissan Murano — keep as-is
x8jd OK: Nissan Pathfinder > Honda Pilot — keep as-is
yx24 OK: Mercedes GLC > Tesla Model X — keep as-is
rr4k OK: Mercedes GLS > BMW X7 — keep as-is
n7wu RECODE: Mercedes GLS > BMW X7 — evidence test_drove_both → owned_one_td_other
d5n6 OK: Cadillac Escalade > BMW X7 — keep as-is
k7jj OK: Range Rover > BMW X7 — keep as-is [model not named — thread inference]
u29d OK: Mercedes GLS > BMW X7 — keep as-is [model not named — thread inference]
y5ny RECODE: Mercedes GLS > BMW X7 — evidence test_drove_both → owned_one_td_other
zwh7 OK: BMW X7 > BMW X5 — keep as-is
z33h OK: Mercedes GLS > BMW X7 — keep as-is
c65y OK: Mercedes GLS > BMW X7 — keep as-is
a7gn OK: Lexus LX > Toyota Sequoia — keep as-is
xd2c OK: Jeep Grand Wagoneer > Lincoln Navigator — keep as-is [model not named — thread inference]
wg6x OK: Cadillac Escalade > Lincoln Navigator — keep as-is
z8wf OK: Lincoln Navigator > Cadillac Escalade — keep as-is
hrv7 OK: Lincoln Navigator > Cadillac Escalade — keep as-is
fgp5 OK: Mercedes GLS > Mercedes GLE — keep as-is
n5yn OK: Cadillac Escalade > Mercedes GLS — keep as-is
y5ca OK: BMW X7 > BMW X5 — keep as-is
a6k3 OK: BMW X7 > BMW X5 — keep as-is
ygc5 OK: Toyota Sequoia > Chevrolet Tahoe — keep as-is
rjr7 OK: Lexus GX > Mercedes GLS — keep as-is
zp5w OK: Lexus GX > Infiniti QX80 — keep as-is
ey3y OK: Lexus GX > BMW X5 — keep as-is
xk6t OK: Mercedes GLE > BMW X5 — keep as-is
a8gs RECODE: Genesis GV80 > BMW X5 — evidence test_drove_both → owned_one_td_other
d9pz OK: Genesis GV80 > Lincoln Aviator — keep as-is
hh82 RECODE: Lexus TX > Lexus GX 550 — home_team 0 → 1
n8k6 RECODE: Lexus TX > Lexus GX — evidence test_drove_both → owned_one_td_other
n8k6 RECODE: Lexus TX > Lexus GX — home_team 0 → 1
tm4t RECODE: Lexus GX > Lexus TX — evidence test_drove_both → owned_one_td_other
tm4t RECODE: Lexus GX > Lexus TX — home_team 0 → 1
jw9w RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
jw9w RECODE: Land Rover Defender > Lexus GX 550 — home_team 0 → 1
b7dm OK: Land Rover Defender > Lexus GX 550 — keep as-is
q3ta OK: Volvo XC90 > Land Rover Defender — keep as-is
xs76 OK: Volvo XC90 > Rivian R1S — keep as-is
f8zj OK: Volvo XC90 > Rivian R1S — keep as-is
apt2 OK: Acura MDX > Rivian R1S — keep as-is
c9zn OK: Genesis GV80 > Rivian R1S — keep as-is
ksp9 QUOTE_FIX: Tesla Model X > Rivian R1S — replace quote with: "Its just a much smoother drive… Quieter… More comfortable seats for long trips… The Rivian has its place, but for 99% of the time for me, the MXP is better."
y9cx OK: Mercedes EQS SUV > BMW iX — keep as-is [model not named — thread inference]
f7p2 OK: Mercedes EQS SUV > BMW iX — keep as-is
dnt5 RECODE: BMW iX > BMW X5 — evidence test_drove_both → owned_one_td_other
az79 RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
e4dn RECODE: Lincoln Aviator > Lexus TX — evidence test_drove_both → owned_one_td_other
e4dn RECODE: Lincoln Aviator > Lexus TX — home_team 0 → 1
hx3e OK: Audi Q8 > BMW X5 — keep as-is
cu6y OK: BMW X5 > Audi Q8 — keep as-is
w9qf OK: Audi Q8 > BMW X5 — keep as-is
c78v RECODE: Porsche Cayenne > BMW X5 — evidence test_drove_both → owned_one_td_other
j7wk RECODE: Genesis GV70 > Lincoln Nautilus — evidence test_drove_both → owned_one_td_other
ce7x OK: Lincoln Nautilus > Genesis GV70 — keep as-is
dy8k OK: Lexus RX > Genesis GV70 — keep as-is
yv74 OK: Genesis GV70 > Lexus NX — keep as-is [model not named — thread inference]
t79x RECODE: Lexus NX > Genesis GV70 — evidence test_drove_both → owned_one_td_other
gdp8 OK: Volvo XC60 > Lexus NX — keep as-is
w99j RECODE: Lexus NX > Toyota RAV4 — evidence test_drove_both → opinion_plus_drive
np9g OK: Lincoln Corsair > Lexus NX — keep as-is
b6fd RECODE: Volkswagen Tiguan > Toyota RAV4 — home_team 0 → 1
dpm4 RECODE: Volkswagen Tiguan > Honda CR-V — evidence test_drove_both → owned_one_td_other
dpm4 RECODE: Volkswagen Tiguan > Honda CR-V — home_team 0 → 1
y2eh OK: Toyota RAV4 > Volkswagen Tiguan — keep as-is
w5rv OK: Lincoln Nautilus > Volkswagen Tiguan — keep as-is
t9yu OK: Mazda CX-9 > Mazda CX-50 — keep as-is
m73t OK: Mazda CX-9 > Mazda CX-50 — keep as-is
w5z9 OK: Lexus NX > BMW X1 — keep as-is
yev8 RECODE: BMW X3 > BMW X1 — evidence test_drove_both → owned_one_td_other
sta9 OK: Porsche Macan > BMW X3 — keep as-is
ba52 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
ph66 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
qwd8 RECODE: Kia Telluride > Kia Sorento — home_team 0 → 1
rfc4 RECODE: Kia Telluride > Kia Sorento — home_team 0 → 1
bqj5 OK: Toyota Highlander > Honda Pilot — keep as-is
jzd8 OK: Buick Enclave > Hyundai Palisade — keep as-is
r7vt OK: Hyundai Palisade > Buick Enclave — keep as-is
stz5 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
ufq2 RECODE: Honda Pilot > Jeep Grand Cherokee L — evidence test_drove_both → owned_one_td_other
b3cz OK: Volkswagen Atlas > Kia Telluride — keep as-is [model not named — thread inference]
rd9z OK: Volkswagen Atlas > Kia Telluride — keep as-is
p9ay RECODE: Volkswagen Atlas > Kia Telluride — evidence test_drove_both → owned_one_td_other
kw94 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
x978 RECODE: Kia Telluride > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
jx45 RECODE: Nissan Pathfinder > Honda Passport — evidence test_drove_both → owned_one_td_other
n4dq OK: Honda Passport > Toyota 4Runner — keep as-is
uhf6 OK: Honda Passport > Toyota 4Runner — keep as-is [model not named — thread inference]
bpa2 OK: Honda Passport > Toyota 4Runner — keep as-is [model not named — thread inference]
u9gy RECODE: Honda Pilot > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
c762 OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
wf98 OK: Volkswagen Atlas > Hyundai Palisade — keep as-is
vv8d OK: Kia Telluride > Toyota 4Runner — keep as-is [model not named — thread inference]
b6d2 OK: Hyundai Palisade > Honda Pilot — keep as-is
kq4s OK: Lexus GX 550 > Toyota Land Cruiser — keep as-is [model not named — thread inference]
kn9p OK: Lexus GX 550 > Toyota Land Cruiser — keep as-is [model not named — thread inference]
m4rr OK: Lexus GX > Lexus GX 550 — keep as-is [model not named — thread inference]
k92g OK: Lexus GX > Volvo XC90 — keep as-is
n3pk OK: Lexus LX > Toyota Sequoia — keep as-is
n3pk RECODE: Lexus LX > Toyota Sequoia — home_team 0 → 1
mxv7 OK: Lexus TX > Toyota Sequoia — keep as-is
mxv7 RECODE: Lexus TX > Toyota Sequoia — home_team 0 → 1
x5ee RECODE: Lexus LX > Toyota Sequoia — evidence owned_one_family → opinion_plus_drive
x5ee RECODE: Lexus LX > Toyota Sequoia — home_team 0 → 1
vx39 RECODE: Buick Enclave > Lexus TX — evidence test_drove_both → owned_one_td_other
vz4g RECODE: Toyota Sequoia > Lexus LX — home_team 0 → 1
v26w OK: Toyota 4Runner > Lexus GX 550 — keep as-is [model not named — thread inference]
av9s RECODE: Lexus GX 550 > Jeep Grand Cherokee L — evidence owned_one_td_other → owned_one_rode_other
ch9x RECODE: Lexus LX > Lexus GX 550 — home_team 1 → 0
qc46 OK: Mercedes GLS > Lexus GX 550 — keep as-is
fn7y OK: Lexus GX > Toyota Land Cruiser — keep as-is
yvz6 OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is
xkt3 OK: Lexus GX > Acura MDX — keep as-is
zu8p OK: Cadillac Escalade > GMC Yukon — keep as-is
n9nj OK: GMC Yukon > Cadillac Escalade — keep as-is [model not named — thread inference]
g6w4 QUOTE_FIX: Cadillac Escalade > GMC Yukon — replace quote with: "I like the button on the Yukon for air. Road noise is better in Escalade but I have a lift and 24s on Yukon. I just think overall specs with the Yukon are just easier with kids!"
uxj6 OK: Lincoln Navigator > Jeep Grand Wagoneer — keep as-is
heu5 OK: Cadillac Escalade > Jeep Grand Wagoneer — keep as-is
kc2k RECODE: Jeep Grand Wagoneer > GMC Yukon — evidence owned_one_td_other → owned_one_family
ae44 OK: Jeep Grand Wagoneer > Chevrolet Tahoe — keep as-is
sh3b RECODE: Chevrolet Tahoe > Lexus GX 550 — evidence owned_one_td_other → opinion
s9sy OK: Buick Enclave > Cadillac XT6 — keep as-is [model not named — thread inference]
atj2 OK: Cadillac Escalade IQ > Lincoln Navigator — keep as-is
g2vq OK: GMC Yukon > Chevrolet Suburban — keep as-is
qqs7 OK: GMC Yukon > Chevrolet Suburban — keep as-is
f94y OK: GMC Yukon > Toyota Sequoia — keep as-is
b73m QUOTE_FIX: Lincoln Navigator > Toyota Sequoia — replace quote with: "The Sequioa, due to the rear suspension, isn't a smooth ride at all."
a3b8 QUOTE_FIX: Infiniti QX80 > Cadillac Escalade — replace quote with: "I personally didn't like the seats in the Escalade, they seemed very grandma to me. I traded in a the rover and the qx80 was more on par with the Interior to me, just much bigger."
ct74 OK: Mercedes EQS SUV > BMW iX — keep as-is [model not named — thread inference]
yz8z RECODE: Mercedes EQS SUV > BMW iX — evidence test_drove_both → owned_one_td_other
m89c RECODE: Genesis GV70 > Porsche Macan — evidence test_drove_both → owned_one_td_other
k3c7 OK: Tesla Model X > Rivian R1S — keep as-is
r74a OK: Rivian R1S > Tesla Model X — keep as-is
aky2 OK: Rivian R1S > Tesla Model X — keep as-is
c35f OK: Tesla Model X > Rivian R1S — keep as-is
d3m2 OK: Land Rover Defender > Porsche Cayenne — keep as-is
f5bt OK: Volvo XC90 > Land Rover Defender — keep as-is
a5ge RECODE: Range Rover Sport > Land Rover Defender — home_team 1 → 0
u579 OK: Land Rover Defender > Range Rover Sport — keep as-is
apj5 OK: Mercedes GLE > Range Rover Sport — keep as-is [model not named — thread inference]
b4gr RECODE: BMW X5 > Porsche Cayenne — evidence test_drove_both → owned_one_td_other
bx3k QUOTE_FIX: BMW X5 > Porsche Cayenne — replace quote with: "my wife preferred the smoothnsss of the X5 over the Cayenne"
pac8 OK: BMW iX > Tesla Model Y — keep as-is
qrc8 OK: Audi Q5 > Porsche Macan — keep as-is [model not named — thread inference]
db6m OK: Volvo XC60 > Rivian R1S — keep as-is [model not named — thread inference]
k865 RECODE: Honda Pilot > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
b556 OK: Honda Pilot > Mazda CX-90 — keep as-is
ghx3 RECODE: Nissan Murano > Nissan Pathfinder — home_team 0 → 1
azh3 OK: Hyundai Palisade > Volkswagen Atlas — keep as-is
fn85 OK: Hyundai Palisade > Mazda CX-90 — keep as-is
bxt8 QUOTE_FIX: Mazda CX-90 > Hyundai Palisade — replace quote with: "A few weeks ago, I test drove the Mazda CX-90 PHEV… everything felt smooth and enjoyable… During the Palisade test drive… it felt slow and heavy compared to the Mazda, not as smooth."
z2h2 OK: Hyundai Palisade > Mazda CX-90 — keep as-is
ya9v RECODE: Nissan Pathfinder > Toyota Highlander — evidence test_drove_both → owned_one_td_other
d3d3 OK: Toyota Highlander > Nissan Pathfinder — keep as-is
bn43 OK: Nissan Pathfinder > Toyota Highlander — keep as-is
e7st RECODE: Nissan Pathfinder > Toyota Highlander — evidence test_drove_both → owned_one_td_other
a5ta QUOTE_FIX: Honda Pilot > Honda Passport — replace quote with: "Test drove both yesterday. Passport is agile but on highway i think pilot is better and quieter"
u776 OK: Honda Pilot > Honda Passport — keep as-is
t8ja QUOTE_FIX: Kia Telluride > Kia Sorento — replace quote with: "Space would be better in the Telluride… I had a Sorento and the 3rd row seats were useless"
sjr4 OK: Honda Pilot > Kia Telluride — keep as-is [model not named — thread inference]
j64e RECODE: Honda Pilot > Toyota Grand Highlander — evidence test_drove_both → owned_one_td_other
k9sz RECODE: Honda Pilot > Mazda CX-90 — evidence test_drove_both → owned_one_td_other
uw78 RECODE: Hyundai Palisade > Buick Enclave — evidence test_drove_both → owned_one_td_other
ac63 OK: Volkswagen Atlas > Honda Pilot — keep as-is
k8nj OK: Tesla Model X > Tesla Model Y — keep as-is
kdx7 OK: Tesla Model X > Tesla Model Y — keep as-is
max6 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
cxy4 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
q5sc OK: Subaru Outback > Subaru Crosstrek — keep as-is
f6yg OK: Subaru Outback > Subaru Crosstrek — keep as-is
kr5k RECODE: Subaru Outback 2026 > Subaru Forester — evidence test_drove_both → owned_one_td_other
kr5k RECODE: Subaru Outback 2026 > Subaru Forester — home_team 0 → 1
x8au OK: Lincoln Corsair > Lexus NX — keep as-is [model not named — thread inference]
q3qt OK: Audi Q5 > Lincoln Corsair — keep as-is
hd37 OK: Lincoln Corsair > Mercedes GLC — keep as-is
k64z QUOTE_FIX: Genesis GV70 > Audi Q5 — replace quote with: "I ended up with the Q5 (somewhat begrudgingly) after trying it along with the X3, XC60, GV70… GV70 was most comfortable by a decent margin with the Volvo in second"
k64z RECODE: Genesis GV70 > Audi Q5 — evidence test_drove_both → owned_one_td_other
x3zy OK: BMW X3 > BMW X1 — keep as-is
rj2c OK: Lexus RX > Cadillac XT5 — keep as-is
qt3m RECODE: Mazda CX-9 > Toyota Highlander — evidence test_drove_both → owned_one_td_other
zk4c OK: Volkswagen Tiguan > Honda CR-V — keep as-is
t3cf OK: Volkswagen Tiguan > Honda CR-V — keep as-is
bj39 OK: Lincoln Nautilus > Lincoln Corsair — keep as-is
b787 RECODE: Lincoln Corsair > Lexus NX — evidence test_drove_both → owned_one_td_other
b8r5 RECODE: Cadillac XT6 > BMW X5 — evidence test_drove_both → owned_one_td_other
zw6n RECODE: Cadillac XT6 > Toyota Highlander — evidence test_drove_both → owned_one_td_other
bm24 OK: Cadillac XT6 > GMC Yukon — keep as-is
ybh2 OK: Cadillac XT6 > Cadillac XT5 — keep as-is
m2ya OK: Subaru Crosstrek > BMW X1 — keep as-is
gun9 OK: GMC Yukon > Cadillac Escalade — keep as-is
c2um OK: Toyota Venza > Toyota RAV4 — keep as-is
aa48 OK: Toyota Highlander > Toyota Venza — keep as-is
vrh3 OK: Subaru Crosstrek > Honda CR-V — keep as-is
rs9b OK: Mazda CX-9 > Toyota RAV4 — keep as-is
ytg7 OK: GMC Yukon > Rivian R1S — keep as-is
ygz9 OK: GMC Yukon > Rivian R1S — keep as-is
k52q OK: GMC Yukon > Rivian R1S — keep as-is
n25t OK: GMC Yukon > Rivian R1S — keep as-is
g7qt OK: GMC Yukon > Rivian R1S — keep as-is
w6wk OK: Rivian R1S > Chevrolet Suburban — keep as-is
s3eg OK: Toyota Sequoia > Chevrolet Tahoe — keep as-is
f2e7 OK: Infiniti QX80 > Cadillac Escalade — keep as-is
dq75 OK: Infiniti QX80 > Chevrolet Tahoe — keep as-is
xf5z OK: GMC Yukon > Toyota Sequoia — keep as-is [model not named — thread inference]
v5yh OK: GMC Yukon > Range Rover — keep as-is
qe3a OK: GMC Yukon > Toyota Sequoia — keep as-is
c85g RECODE: GMC Yukon > Lexus GX — home_team 0 → 1
tp5u OK: Cadillac Escalade > Chevrolet Tahoe — keep as-is
sp4e OK: Chevrolet Tahoe > Toyota Sequoia — keep as-is
dsc8 OK: Range Rover > Toyota Sequoia — keep as-is
r3n8 OK: GMC Yukon > Lexus GX — keep as-is
kaz7 QUOTE_FIX: Lexus RX > Lexus GX 550 — replace quote with: "I've test drive both twice. I enjoy both. The GX does ride a little rougher on the same road but that is too be expected."
egj2 OK: GMC Yukon > Cadillac Escalade — keep as-is
px2e OK: Rivian R1S > Tesla Model X — keep as-is
t6vw OK: Rivian R1S > Tesla Model X — keep as-is
u5nk OK: Range Rover Sport > Land Rover Defender — keep as-is
ynz3 OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
e7cy OK: Range Rover > Land Rover Defender — keep as-is
v4rk OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
csp4 OK: Range Rover > Land Rover Defender — keep as-is [model not named — thread inference]
ppr9 OK: Range Rover Sport > Land Rover Defender — keep as-is
a8kk OK: Audi Q5 > Genesis GV70 — keep as-is
g536 RECODE: Porsche Cayenne > Mercedes GLE AMG — evidence test_drove_both → owned_one_td_other
h238 OK: BMW X5 > Porsche Cayenne — keep as-is
q4w8 OK: Porsche Cayenne > BMW X5 — keep as-is
tpe8 OK: BMW X7 > Porsche Cayenne — keep as-is
u23t OK: BMW X5 > Porsche Cayenne — keep as-is
tt82 OK: Mercedes GLE > BMW X5 — keep as-is
bhg5 OK: Mercedes GLE > Porsche Cayenne — keep as-is
csm9 OK: Mercedes GLE > BMW X5 — keep as-is
k2gz RECODE: Mercedes GLE > BMW X5 — evidence test_drove_both → owned_one_td_other
kz5e OK: BMW X5 > Mercedes GLE — keep as-is
ja4q DELETE: Mercedes GLE > BMW X5 — remove row
fgy4 RECODE: BMW X5 > Porsche Cayenne — evidence test_drove_both → owned_one_td_other
nt52 OK: Mercedes GLE > BMW X5 — keep as-is
pe4z RECODE: Mercedes GLE > Jeep Grand Cherokee — evidence test_drove_both → owned_one_td_other
g36p RECODE: Jeep Grand Cherokee > BMW X5 — evidence test_drove_both → owned_one_td_other
zwc6 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
qp57 RECODE: Subaru Outback > Subaru Crosstrek — home_team 0 → 1
u56y OK: Subaru Outback > Subaru Crosstrek — keep as-is
bk6n OK: Subaru Outback > Subaru Crosstrek — keep as-is
w743 RECODE: Subaru Outback > Subaru Crosstrek — evidence owned_one_loaner → opinion_plus_drive
cn8t RECODE: Cadillac XT6 > Cadillac XT5 — home_team 0 → 1
bwm5 OK: Tesla Model X > Tesla Model Y — keep as-is
gr8w OK: Tesla Model X > Tesla Model Y — keep as-is
czk8 OK: Tesla Model X > Tesla Model Y — keep as-is
drx4 OK: Tesla Model X > Tesla Model Y — keep as-is
cmy5 RECODE: Lincoln Corsair > Volvo XC60 — evidence test_drove_both → owned_one_td_other
zxu2 OK: Nissan Murano > Nissan Pathfinder — keep as-is [model not named — thread inference]
h6k9 OK: Nissan Murano > Nissan Pathfinder — keep as-is
hgd3 OK: Nissan Pathfinder > Nissan Murano — keep as-is
c3nc OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
y6nr OK: Lexus NX > Mazda CX-5 — keep as-is
u52r OK: Subaru Outback > Subaru Forester — keep as-is
kx75 OK: Honda CR-V > Subaru Forester — keep as-is
uap3 OK: Subaru Forester > Subaru Crosstrek — keep as-is
bdj8 OK: Subaru Forester > Subaru Crosstrek — keep as-is
y697 OK: BMW X1 > BMW X3 — keep as-is
y697 RECODE: BMW X1 > BMW X3 — home_team 0 → 1
q7ty OK: Kia Telluride > Toyota RAV4 — keep as-is
x297 OK: Volvo XC90 > Tesla Model Y — keep as-is
c2sv QUOTE_FIX: Mazda CX-90 > Kia Telluride — replace quote with: "The difference in road noise, the power and performance, and comfort are all better."
y2ug OK: Honda Pilot > Mazda CX-90 — keep as-is
mqd3 OK: Honda Pilot > Mazda CX-90 — keep as-is
t5ys OK: Honda Pilot > Jeep Grand Cherokee L — keep as-is
qp66 QUOTE_FIX: Hyundai Palisade > Buick Enclave — replace quote with: "We test drove the Enclave and were not impressed. It's a 4 cylinder engine and the vehicle can't get out of its own way and makes a tom of noise. We were a Buick family until 2026 and now own a Pslisade."
kk23 OK: Hyundai Palisade > Kia Telluride — keep as-is
j6ta RECODE: Hyundai Palisade > Kia Telluride — evidence test_drove_both → owned_one_td_other
yxe3 QUOTE_FIX: Kia Telluride > Mazda CX-90 — replace quote with: "Had 2022 Telluride, traded in for 2024 CX-90 PHEV… The only reason I switched from Telluride to CX90 is cost savings… Other than that, Telluride is way more comfortable, more spacious…"
h9jh OK: Kia Telluride > Toyota 4Runner — keep as-is
rv98 RECODE: Toyota Grand Highlander > Honda Pilot — evidence test_drove_both → owned_one_td_other
ds7n OK: Hyundai Palisade > Honda Pilot — keep as-is
as4g OK: Kia Telluride > Hyundai Palisade — keep as-is
as4g RECODE: Kia Telluride > Hyundai Palisade — home_team 0 → 1
e3d3 OK: Cadillac XT6 > Cadillac XT5 — keep as-is [model not named — thread inference]
b8bk RECODE: Ford Explorer > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
q365 OK: Ford Explorer > Toyota 4Runner — keep as-is
q365 RECODE: Ford Explorer > Toyota 4Runner — home_team 0 → 1
d5t3 RECODE: Hyundai Palisade > Honda Pilot — evidence test_drove_both → owned_one_td_other
s4a3 RECODE: Honda Pilot > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
utg4 OK: Mazda CX-5 > Mazda CX-90 — keep as-is
t4uj OK: Honda Passport > Honda Pilot — keep as-is
d7ex RECODE: Ford Explorer > Toyota Highlander — evidence test_drove_both → owned_one_td_other
bfv8 RECODE: Toyota Highlander > Ford Explorer — evidence test_drove_both → owned_one_td_other
zkc5 RECODE: Buick Enclave > Kia Telluride — evidence test_drove_both → owned_one_td_other
jpa9 RECODE: Buick Enclave > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
y3df OK: Mazda CX-9 > Honda Pilot — keep as-is
p939 RECODE: Mazda CX-9 > Toyota Highlander — evidence test_drove_both → owned_one_td_other
h7zh RECODE: Mazda CX-9 > Nissan Pathfinder — evidence test_drove_both → owned_one_td_other
nqc3 OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
kg8w OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
kg8w RECODE: Cadillac Escalade IQ > Tesla Model X — home_team 0 → 1
m5tx OK: Cadillac Escalade IQ > Cadillac Escalade — keep as-is [model not named — thread inference]
r3ab OK: Cadillac Escalade IQ > Tesla Model X — keep as-is
p4fc OK: Mercedes GLE AMG > BMW X5 — keep as-is
p4fc RECODE: Mercedes GLE AMG > BMW X5 — home_team 0 → 1
p9gr OK: Mercedes GLS > Mercedes GLE AMG — keep as-is
p9gr RECODE: Mercedes GLS > Mercedes GLE AMG — home_team 0 → 1
gq5z OK: BMW X5 > Mercedes GLE — keep as-is
xen5 OK: Lexus GX > Toyota Land Cruiser — keep as-is
xen5 RECODE: Lexus GX > Toyota Land Cruiser — home_team 0 → 1
h4pt OK: Toyota 4Runner > Toyota Land Cruiser — keep as-is
hj76 OK: Toyota Land Cruiser > Toyota 4Runner — keep as-is
y8sv QUOTE_FIX: Lexus LX > Toyota Sequoia — replace quote with: "Not apples to apples, but I have a LX 700 and a Sequoia, both 2025s. My wife and I prefer the Lexus while our kids prefer the Sequoia… The biggest differences are noise, ride comfort, and space."
e6ff OK: Lexus LX > Toyota Land Cruiser — keep as-is [model not named — thread inference]
ppw3 OK: GMC Yukon > Toyota Sequoia — keep as-is
av5z QUOTE_FIX: GMC Yukon > Chevrolet Tahoe — replace quote with: "The Yukon entertainment system screen is worlds better than Chevy amd the fit and finish is better to… I also feel the road noise is quieter in the Yukon than Chevy."
x3fn QUOTE_FIX: Range Rover > Land Rover Defender — replace quote with: "I have both. I love my RR much more."
s6pu OK: Land Rover Defender > Porsche Cayenne — keep as-is
s4kp OK: Range Rover > Porsche Cayenne — keep as-is [model not named — thread inference]
y4g6 OK: Mercedes GLE > Porsche Cayenne — keep as-is
f2u2 OK: Land Rover Defender > Porsche Cayenne — keep as-is
rx27 OK: Jeep Grand Cherokee > BMW X5 — keep as-is
rx27 RECODE: Jeep Grand Cherokee > BMW X5 — home_team 0 → 1
d4wb OK: BMW X5 > Tesla Model Y — keep as-is
p5sz OK: Jeep Grand Cherokee > Tesla Model Y — keep as-is
d6mz OK: Land Rover Defender > Rivian R1S — keep as-is
fmy7 OK: BMW X5 > Rivian R1S — keep as-is
ux26 OK: BMW iX > Rivian R1S — keep as-is [model not named — thread inference]
y4hu RECODE: Genesis GV70 > Porsche Macan — evidence test_drove_both → owned_one_td_other
y4hu RECODE: Genesis GV70 > Porsche Macan — home_team 0 → 1
r3eu RECODE: Porsche Macan > Audi Q5 — evidence test_drove_both → owned_one_td_other
c5nh RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
b4sx OK: Volkswagen Tiguan > Honda CR-V — keep as-is
b4sx RECODE: Volkswagen Tiguan > Honda CR-V — home_team 0 → 1
nt9a OK: Volkswagen Tiguan > Toyota RAV4 — keep as-is
nt9a RECODE: Volkswagen Tiguan > Toyota RAV4 — home_team 0 → 1
yta9 OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
yta9 RECODE: Volkswagen Tiguan > Mazda CX-5 — home_team 0 → 1
h6c4 OK: Toyota Venza > Toyota RAV4 — keep as-is
h6c4 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
wsa7 OK: Toyota Venza > Toyota RAV4 — keep as-is
wsa7 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
bp9e OK: Lincoln Nautilus > Lincoln Corsair — keep as-is
bp9e RECODE: Lincoln Nautilus > Lincoln Corsair — home_team 0 → 1
tdu3 OK: Mercedes GLC > BMW X3 — keep as-is
tdu3 RECODE: Mercedes GLC > BMW X3 — home_team 0 → 1
v44q OK: Honda CR-V > Subaru Crosstrek — keep as-is
b3b4 OK: Subaru Crosstrek > Subaru Forester — keep as-is
b3b4 RECODE: Subaru Crosstrek > Subaru Forester — home_team 0 → 1
t8rw OK: BMW X3 > BMW X1 — keep as-is
t8rw RECODE: BMW X3 > BMW X1 — home_team 0 → 1
h9y8 OK: BMW X5 > BMW X1 — keep as-is
h9y8 RECODE: BMW X5 > BMW X1 — home_team 0 → 1
rgp7 OK: BMW X5 > BMW X3 — keep as-is
rgp7 RECODE: BMW X5 > BMW X3 — home_team 0 → 1
qn4x QUOTE_FIX: Subaru Outback 2026 > Subaru Forester — replace quote with: "The Outback Premium felt more comfortable and more upscale, partly because the Premium trim includes the nicer StarTex interior. It also seemed better for road trips and family cargo."
qn4x RECODE: Subaru Outback 2026 > Subaru Forester — home_team 0 → 1
mey2 QUOTE_FIX: Subaru Outback > Subaru Forester — replace quote with: "For me it's the ride quality and handling. Forester is nice for short trips. Outback is nice for long trips. The Outback has way more comfortable seats imo."
mey2 RECODE: Subaru Outback > Subaru Forester — home_team 0 → 1
wny8 OK: Nissan Murano > Tesla Model X — keep as-is
wny8 RECODE: Nissan Murano > Tesla Model X — home_team 0 → 1
t3af OK: Buick Enclave > BMW X5 — keep as-is
snx3 RECODE: Jeep Grand Cherokee L > Hyundai Palisade — evidence test_drove_both → owned_one_td_other
s8kn RECODE: Jeep Grand Cherokee L > Kia Telluride — evidence test_drove_both → owned_one_td_other
x32s RECODE: Cadillac XT5 > BMW X3 — axis seats → overall
x32s RECODE: Cadillac XT5 > BMW X3 — evidence owned_one_td_other → owned_both
uf6x QUOTE_FIX: Mercedes EQS SUV > BMW iX — replace quote with: "We've had both-a 2023 EQS suv and our 2025 iX50. … Seats are legit terrible … Seats were incredible-massages, pillows etc"
aca7 OK: Mercedes EQS SUV > Rivian R1S — keep as-is
u5ak OK: Subaru Crosstrek > Subaru Outback — keep as-is
aaw6 OK: Subaru Outback > Subaru Crosstrek — keep as-is
n6s7 OK: Cadillac Escalade IQ > Cadillac Escalade — keep as-is
q83z RECODE: Range Rover > Land Rover Defender — evidence test_drove_both → owned_one_td_other
md87 OK: BMW X5 > Tesla Model Y — keep as-is
c83x OK: BMW X5 > Tesla Model Y — keep as-is
uqa6 OK: Land Rover Defender > Rivian R1S — keep as-is
prc3 OK: BMW X5 > Rivian R1S — keep as-is
b8jz OK: Porsche Macan > Audi Q5 — keep as-is
ft3r RECODE: Land Rover Defender > Lexus GX 550 — evidence test_drove_both → owned_one_td_other
nqw8 OK: Volkswagen Tiguan > Mazda CX-5 — keep as-is
nqw8 RECODE: Volkswagen Tiguan > Mazda CX-5 — home_team 0 → 1
mbq2 OK: Toyota Venza > Toyota RAV4 — keep as-is
mbq2 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
x4ne RECODE: Toyota Venza > Toyota RAV4 — evidence test_drove_both → owned_one_td_other
x4ne RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
zq5z OK: Toyota Venza > Toyota RAV4 — keep as-is
zq5z RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
ebb4 OK: Toyota Venza > Toyota RAV4 — keep as-is
ebb4 RECODE: Toyota Venza > Toyota RAV4 — home_team 0 → 1
cfb9 RECODE: Lincoln Nautilus > Lincoln Corsair — evidence test_drove_both → owned_one_td_other
cfb9 RECODE: Lincoln Nautilus > Lincoln Corsair — home_team 0 → 1
s95d OK: Mercedes EQS SUV > BMW iX — keep as-is
s47c RECODE: Mercedes EQS SUV > Rivian R1S — evidence test_drove_both → owned_one_td_other
khh6 OK: Range Rover > Mercedes GLS — keep as-is [model not named — thread inference]
tz96 QUOTE_FIX: Audi Q7 > BMW X5 — replace quote with: "I test drove the X5 and Q7 today and the X5 LOOKS better but the Q7 FEELS better"
f4d4 QUOTE_FIX: Genesis GV80 > BMW X5 — replace quote with: "I've driven all three and in the end we went with the x5m50i because of the performance Factor. … Gv80 was a little cushier than we preferred"
f4d4 RECODE: Genesis GV80 > BMW X5 — evidence test_drove_both → owned_one_td_other
a9cg QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "The Hybrid Palisade, though was a completely different animal. … But the real showstopper is the ride quality. The chassis just glides over bumps and imperfections; it truly soaks everything up. My old Tucson and even the santafe I test drove would feel jittery on these same roads."
q3sa QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "The Palisade drives wonderfully and is quiet, while the Santa Fe is more sporty but still smooth and quiet."
ssb9 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "We did 2 test drives with each and were sold by the Palisade (2026) easily. … The ride is much, much smoother as well. The Santa Fe feels zippy to drive, but you feel every bump on the road."
ssb9 RECODE: Hyundai Palisade > Hyundai Santa Fe — evidence test_drove_both → owned_one_td_other
c793 QUOTE_FIX: Hyundai Palisade > Hyundai Santa Fe — replace quote with: "It's comfortable just the right size. … Palisade is also very nice. Quieter and smoother but not by too much."
p6n7 QUOTE_FIX: Ford Expedition > Chevrolet Suburban — replace quote with: "the Yukon and Suburban (we owned a Suburban, rented a Yukon Denali for a week to get a feel before buying the Expedition) just drove like they were too top heavy and about to tip on any curve going over 55… The Expedition grips the road and you just feel steady and more level"
vd8w QUOTE_FIX: Chevrolet Suburban > Ford Expedition — replace quote with: "The Suburban rides smoother and softer, handles better… Chevy uses MUCH better tires (Michelin Primacy) than Ford (hankook Dynapro ATM) on the examples I've rented. Those dynapros are loud!!"
s9zb QUOTE_FIX: Ford Expedition > Chevrolet Tahoe — replace quote with: "When sitting in the expy the seats are noticeably better. I did not get to test drive a max so not sure the ride quality compared to standard. I prefer the looks of the Tahoe and features of the expedition."
tyk8 QUOTE_FIX: Cadillac Escalade > Ford Expedition — replace quote with: "It felt like I was driving a van—every bump in the road was noticeable. Compared to my Escalade, which has a much smoother ride, the Expedition's suspension felt rough and unrefined."
kub5 QUOTE_FIX: Lincoln Navigator > Ford Expedition — replace quote with: "I test drove a bunch of different exp trims… I decided on a navigator L reserve trim w/ luxury package and it's a much better driving experience than a platinum trim expedition."
kub5 RECODE: Lincoln Navigator > Ford Expedition — evidence test_drove_both → owned_one_td_other
qe2j QUOTE_FIX: Ford Expedition > Chevrolet Suburban — replace quote with: "the interior is nicer and much more comfortable. I won't knock the GMs i had, they were good vehicles but we gambled on a switch to the expedition and my wife wishes we would have done it sooner."
