# ForkFox Master Plan: Business Portal + Go-To-Market + Channel Tactics

## 0) Executive Read: What’s Going On Right Now

### Operational reality (from the CC logs/context)
- You had a sequencing failure, not a strategy failure: social scheduling fired before OG image deploy completion.
- Facebook failed early because it validates image URLs at schedule-time; Pinterest tolerated deferred validation.
- Recovery pattern that worked: ignore unsupported Ayrshare retry/delete flows on your plan tier, and re-submit fresh posts after Vercel served `200 OK` on OG assets.
- Current state (per your context): 13 articles × 2 channels = 26 pending scheduled posts, with lockfiles protecting against duplicate scheduling.

### Strategic implication
- Your issue was pipeline orchestration reliability, not content-market fit.
- Immediate corrective product need: **publish gating** (only schedule once asset health checks pass) + **idempotent scheduling ledger** (not just lockfiles).

---

## 1) What I reviewed on forkfox.ai (and how to use it in marketing)

### Positioning that is already strong
- Core thesis is clear and differentiated: **"They rank restaurants. We rank what you actually eat."**
- Narrative consistency across homepage, algorithm section, and support copy: dish-level scoring, personalized ranking, explainability (spider chart), and city expansion.
- Tangible product proof: iOS beta framing, dish/city counts, clear use-case examples.

### Trust signals already present
- Patent-pending claim repeated.
- Clear privacy/support pages and plain-language data policy.
- Explicit no-sale/no-ad-network language in privacy copy.

### Gaps to tighten for growth conversion
1. **Proof density gap**: Add stronger public evidence blocks (before/after restaurant outcomes, sample leaderboard deltas, retention stats).
2. **B2B bridge gap**: Consumer site says little about a restaurant-facing portal opportunity.
3. **CTA depth gap**: “Join Beta” is clear, but follow-up journey could segment users by role (consumer vs owner/operator).
4. **Market education gap**: Explainability is strong, but onboarding should quickly teach why dish-level scoring changes owner behavior and campaign ROI.

---

## 2) Product Strategy for the Business Portal (Strategic Intelligence, not day-trading)

Because scrapes are not daily, the portal should center on:
1. **Drift over tick data** (directional intelligence),
2. **Anomaly alerts** (urgent exceptions),
3. **Action modules** that convert insight into revenue (coupons, placements, social assets).

### North Star outcomes
- Increase operator retention via “I know what improved and why.”
- Increase monetization via self-serve paid tools.
- Increase marketplace quality by rewarding high-performing dishes and operators.

---

## 3) Build Roadmap by Gate (What to build this week → Gate 4)

## Gate 1 (Week 1–2): MVP That Delivers Immediate Utility
**Goal:** Ship value quickly with minimal engineering risk.

### Build this week
1. **Command Center (read-only intelligence + 2 actions)**
   - Anchor Dish Health score + last refresh timestamp.
   - YoY momentum card from sentiment engine (e.g., +15% YoY with top driver).
   - “Top 3 risk factors” and “Top 3 strengths.”
2. **Basic Competitor Snapshot**
   - You vs top 3 competitors on core attributes.
   - Gap-to-leader metric by dish category.
3. **Quick Actions (fast wins)**
   - Social badge generator (3 templates).
   - Exportable summary (PDF/email card) for weekly ops meetings.
4. **Pipeline Hardening (must-have)**
   - Pre-schedule asset validator (OG URL health check).
   - Idempotent scheduling table (`post_key`, platform, scheduled_at, status).
   - Retry model that avoids unsupported endpoints.

### Gate 1 acceptance criteria
- Owner logs in and gets 3 clear recommendations in under 30 seconds.
- One-click share asset exported successfully.
- No duplicate schedules across reruns.

---

## Gate 2 (Week 3–5): Revenue Tools + Better Diagnostics
**Goal:** Move from intelligence dashboard to ROI-producing workflow.

### Features
1. **Coupon Factory**
   - Rules-based templates tied to score thresholds.
   - Example: “Free drink with any 90+ dish order.”
   - Track redemption code + attributable lift.
2. **Placement Management (self-serve)**
   - Eligibility checks (quality floor, review volume, policy compliance).
   - Suggested bid ranges from category competition.
3. **Competitor Battle Map (enhanced)**
   - 2mi / 5mi radius snapshot.
   - “Position held for X days” metric.
   - Event markers (“competitor launched spring menu”).
4. **Alerting Engine v1**
   - Anomaly-only notifications (e.g., high-risk sentiment spike).
   - Configurable severity and channel (email/SMS/slack/webhook).

### Gate 2 acceptance criteria
- At least one monetizable action (coupon or placement) can be launched without manual ops.
- Alert triage reduces “time-to-owner-awareness” below 1 hour for critical events.

---

## Gate 3 (Week 6–9): Pro Intelligence + Team Workflows
**Goal:** Make the portal sticky for multi-location operators and agencies.

### Features
1. **Sentiment Deep Dive (your proprietary engine)**
   - Scatter plot (frequency × sentiment).
   - Driver decomposition (“wait time down 22% drove +15% score delta”).
   - Theme cohorts by meal period/daypart.
2. **Multi-location rollups**
   - Portfolio health view.
   - Location variance and top outliers.
3. **Tasking + workflow notes**
   - Assign follow-ups (“Chef: improve broth consistency this week”).
   - Weekly summary digest with action statuses.
4. **API/Webhook exports**
   - Push key metrics to BI tools / CRM / ad systems.

### Gate 3 acceptance criteria
- Weekly owner review can run entirely from portal exports + workflows.
- At least 2 stakeholder roles (operator + marketer) actively use portal weekly.

---

## Gate 4 (Quarter 2+): Optimization Flywheel + Marketplace Advantage
**Goal:** Build defensibility and pricing power.

### Features
1. **Predictive forecasts**
   - “If wait-time mentions improve 10%, expected score lift = X.”
2. **Recommendation engine for interventions**
   - Menu, staffing, and service suggestions ranked by impact.
3. **Budget optimizer**
   - Allocation suggestions across placements, coupons, and social channels.
4. **Benchmark network intelligence**
   - Anonymous category benchmarks by city/cuisine/daypart.

### Gate 4 acceptance criteria
- Portal can attribute revenue impact to specific actions with confidence intervals.
- Expansion to premium/enterprise tiers justified by measurable lift.

---

## 4) Wireframes by Function and Phase

## A) Command Center (Gate 1)
```text
+--------------------------------------------------------------------------------+
| ForkFox Business Portal                                     Last refresh: 3d    |
+--------------------------------------------------------------------------------+
| Anchor Dish Health: 78/100   [Trend: +4.2 vs last scrape]   [Status: Stable]    |
| YoY Sentiment: +15% (Apr 2026 vs Apr 2025)                                       |
| Primary Driver: Wait-time mentions -22%                                          |
+--------------------------------------------------------------------------------+
| Top Strengths                     | Top Risks                                    |
| - Noodle texture (+)              | - Friday dinner noise (rising)              |
| - Flavor consistency (+)          | - Portion value complaints (+11%)           |
| - Service friendliness (+)        | - Late-night prep speed (-)                 |
+--------------------------------------------------------------------------------+
| Quick Actions: [Generate Social Badge] [Respond to At-Risk Reviews] [Export PDF] |
+--------------------------------------------------------------------------------+
```

## B) Competitor Dashboard / Battle Map (Gate 1→2)
```text
+--------------------------------------------------------------------------------+
| Competitive Position (2mi / 5mi)                   Last competitive scrape: 3d  |
+--------------------------------------------------------------------------------+
| You: #2 Best Ramen (held 14 days)                                              |
| Leader Gap: -6 on Meat Quality | +12 on Atmosphere                             |
+--------------------------------------------------------------------------------+
| Radar Compare: You vs Competitor A vs Competitor B                              |
| [Taste] [Value] [Service] [Wait Time] [Consistency]                             |
+--------------------------------------------------------------------------------+
| Event Feed                                                                     |
| - Competitor Y launched Spring Special menu                                    |
| - Competitor B ratings dipped in dinner hour                                   |
+--------------------------------------------------------------------------------+
```

## C) Growth Tools Hub (Gate 2)
```text
+--------------------------------------------------------------------------------+
| Growth Tools                                                                    |
+--------------------------------------------------------------------------------+
| Coupon Factory                         | Placement Bidder                        |
| Eligible: Yes (Quality 92)             | Eligible: Yes (Org score 85 vs med 78) |
| [Create Offer]                         | [Bid for Carte Placement]               |
+--------------------------------------------------------------------------------+
| Badge Studio                                                                  |
| Templates: Modern / Minimal / Traditional / Street / Premium                  |
| [Generate Asset Pack] [Schedule to FB/Pinterest/IG]                           |
+--------------------------------------------------------------------------------+
```

## D) Sentiment Intelligence Lab (Gate 3)
```text
+--------------------------------------------------------------------------------+
| Sentiment Intelligence (Pro)                                                   |
+--------------------------------------------------------------------------------+
| Bubble Plot: Frequency vs Sentiment                                            |
| Winner: Noodle Texture (high freq, high sentiment)                             |
| Warning: Friday Dinner Noise (rising freq, low sentiment)                      |
+--------------------------------------------------------------------------------+
| Driver Decomposition                                                            |
| +15% YoY overall improvement due to:                                            |
| - Wait time improvements (41%)                                                  |
| - Service consistency (27%)                                                     |
| - Plate temperature quality (13%)                                               |
+--------------------------------------------------------------------------------+
| Recommended Actions: [Staffing Plan] [Menu Copy Update] [Social Narrative]     |
+--------------------------------------------------------------------------------+
```

## E) Multi-location Portfolio (Gate 3)
```text
+--------------------------------------------------------------------------------+
| Portfolio Health: 8 locations                                                   |
+--------------------------------------------------------------------------------+
| Avg Dish Health: 81 (+3)  | Highest: Rittenhouse | Risk: University City        |
| Location variance: 14 pts (target <10)                                          |
+--------------------------------------------------------------------------------+
| Table: location | health | YoY | risk index | open tasks                         |
+--------------------------------------------------------------------------------+
```

---

## 5) End-to-End Marketing Strategy (Integrated with Product Gates)

## Brand narrative (single sentence)
**ForkFox helps diners choose better dishes and helps restaurants improve what actually drives repeat business — dish by dish.**

## Messaging pillars
1. **Precision over averages** (dish-level vs restaurant stars).
2. **Explainability** (score anatomy, not black-box outputs).
3. **Actionability** (what to do next to improve).
4. **Outcome focus** (better dining choices + measurable operator lift).

---

## 6) Channel Tactics (what to do by channel)

## A) Owned channels
### Website
- Add B2B nav entry: “For Restaurants.”
- Add dual CTA fork: “Join Beta (Diners)” vs “Request Business Demo.”
- Add proof blocks: operator outcomes, sample dashboard screenshots, benchmark snippets.

### Email lifecycle
- **Diner onboarding:** 3-email sequence (how scores work, personalized tips, invite to share).
- **Operator onboarding:** 5-email sequence (dashboard walkthrough, quick wins, first campaign template).
- Weekly digest: “What changed since last scrape + what to do next.”

### In-app
- Highlight “why this changed” for every major score movement.
- Contextual prompts to launch coupons/badges when thresholds met.

## B) Social channels
### LinkedIn (B2B authority)
- 3 posts/week:
  - Dish-vs-restaurant insight snapshots,
  - “Operator play of the week,”
  - Short case breakdowns with metric deltas.

### Instagram + TikTok (consumer discovery)
- 4–5 short-form posts/week:
  - Side-by-side “same stars, different dishes,”
  - City micro-guides,
  - Community “best plate under $15” challenges.

### X/Twitter (thought leadership + product velocity)
- Build-in-public threads on algorithm explainability, city launches, and data stories.
- Weekly founder thread: 1 market insight + 1 product update + 1 CTA.

### Pinterest (evergreen intent)
- Maintain scheduled “city dish cards,” “budget picks,” and cuisine boards.
- Pair each pin with long-tail keywords and city/cuisine taxonomy.

## C) Partnerships & field growth
- Pilot with 10–20 restaurants per launch city.
- Co-marketing with food creators (dish challenge series by cuisine).
- Hospitality-tech integrations (reservation/waitlist POS-adjacent partnerships).

## D) Paid acquisition (after baseline retention)
- Small-budget experiments:
  - Meta/IG for city-level consumer acquisition,
  - LinkedIn lead-gen forms for operator demos,
  - Branded search + competitor search on Google.
- Keep spend gated by CAC payback targets and activation metrics.

---

## 7) KPI Framework by Gate

## Gate 1 KPIs
- Business portal weekly active operators (WAO).
- Time-to-first-insight (<30s target).
- Quick action conversion rate (badge export, review response).

## Gate 2 KPIs
- Coupon launch rate + redemption lift.
- Placement participation rate + incremental CTR/bookings.
- Critical alert response time.

## Gate 3 KPIs
- Multi-seat account retention.
- Action completion rate from recommendations.
- Lift attribution confidence for intervention categories.

## Gate 4 KPIs
- Forecast accuracy bands.
- Revenue attributed to optimized spend recommendations.
- Expansion revenue (Pro/Enterprise).

---

## 8) Immediate 14-Day Tactical Sprint

### Days 1–3
- Ship Gate 1 Command Center UI skeleton.
- Add post-schedule health checks and idempotency ledger.
- Build 3 social badge templates.

### Days 4–7
- Launch competitor snapshot + basic gap analysis.
- Launch weekly digest email with "what changed / why / what to do".
- Publish first B2B landing section on site.

### Days 8–10
- Pilot Coupon Factory with a rules template.
- Configure anomaly alerts for high-severity review clusters.

### Days 11–14
- Run 5-operator pilot walkthroughs.
- Capture testimonials + outcome metrics.
- Prepare Gate 2 implementation backlog from live feedback.

---

## 9) Investor/Board Narrative (tight)

1. **Problem:** Restaurant-level stars are too coarse to drive operational improvement.
2. **Insight:** Dish-level quality intelligence is more predictive of choice and repeat behavior.
3. **Product:** Consumer ranking + business intelligence portal.
4. **Moat:** Proprietary attribute graph, explainable scoring, and feedback-to-action loop.
5. **Monetization:** SaaS intelligence + placements + campaign tools.
6. **Scale path:** City expansion + multi-location operator expansion.

---

## 10) Guardrails & Risks to manage now
- Do not imply real-time when data is periodic; be explicit with freshness labels.
- Keep explainability readable (operators need plain language, not model jargon).
- Add strong QA for social asset URLs before scheduling.
- Ensure lockfiles are backed by persistent scheduling records to avoid ghost duplicates.

---

## 11) Recommended next deliverables
1. Clickable Figma-style prototype for Gate 1 + Gate 2 screens.
2. A/B copy set for B2C vs B2B landing paths.
3. 30-day channel calendar (LinkedIn/IG/X/Pinterest).
4. Pilot sales one-pager for restaurant onboarding.
