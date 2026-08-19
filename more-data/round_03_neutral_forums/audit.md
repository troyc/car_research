# Round 03 neutral-forum audit

Collection date: 2026-08-19. Scope was ordinary, public, browser-readable thread HTML on Bob Is The Oil Guy and Edmunds Forums. No login, member/profile, search, API, print, post, CAPTCHA, proof-of-work, or challenge endpoints were used. Direct requests were not used; the web reader surfaced public pages from targeted search results. Raw usernames are not stored anywhere in this round; included rows use only deterministic respondent hashes, and rejected rows have no respondent identifiers.

## Access, robots, and terms checks

- Bob Is The Oil Guy: the browser reader could not safely open the root `robots.txt` URL, so no crawling or endpoint probing was attempted. The current public [forum rules](https://www.bobistheoilguy.com/forum-rules/) state that the site does not permit data-mining/scraping-like use and prohibit activity that could damage, disable, overburden, or impair servers. Collection was limited to manually targeted ordinary thread pages and review excerpts.
- Edmunds Forums: the browser reader could not safely open the forum subdomain's root `robots.txt`; the current public robots scan records a live `edmunds.com/robots.txt` and query-parameter restrictions. Edmunds' [Forums Rules of the Road](https://forums.edmunds.com/discussion/56333/general/x/edmunds-forums-rules-of-the-road) require on-topic, courteous posts and prohibit spam. The [Visitor Agreement](https://www.edmunds.com/about/visitor-agreement.html) grants personal access but expressly prohibits robots, scraping, data mining, and collection of visitor content; it allows only occasional short excerpts with the original page available.

## Discovery and inclusion

Targeted searches were reviewed in small batches (well below 25 threads per source). The round retains two current-era BITOG rows: Crosstrek over CX-5 on ride and Atlas over Grand Cherokee L on ride. The latter is a same-day direct drive of both Atlas engine offerings and a Grand Cherokee L; the poster explicitly called the Jeep's ride much firmer and preferred the six-cylinder Atlas. A later cross-segment pass found unusually detailed X5/Atlas/Sequoia seat and long-trip passages from one owner, but direct reply context identified the X5 as a 2013 model and the Sequoia as a 2018 model; those comparisons were logged as generation drift rather than mixed into the contemporary nodes. Two CR-V rear-seat-fit rows were rejected because the post did not establish a test drive or another existing first-hand evidence category. Five Edmunds passages were historical 2000–08 generations incompatible with the contemporary model scopes in the current graph. The BITOG Explorer/Palisade passage distinguishes handling (“athletic” versus “mushy”) rather than a comfort/ride-compliance winner and was rejected. A Traverse-versus-Grand Cherokee L seat passage was rejected because Traverse is outside the canonical model map. Additional shopping, equipment, reliability, or unsupported opinions are recorded in `rejections.csv`.

The required comparisons/context files contain two included rows with aligned IDs and populated audit context. No generated parent data or ranking output was changed.

## Open gaps

No additional current-generation qualified neutral-forum evidence was found for the requested sparse pairs or long-trip targets after the cross-segment pass and source-policy constraints. Future collection should prioritize browser-readable first-person passages that state model years and an explicit comfort-axis winner.
