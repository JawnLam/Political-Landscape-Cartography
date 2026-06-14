# 0458 — THE 'DEFINITION OF DONE' WARFARE

> Continuously altering the completion criteria or success metrics for a rival's project just as they approach the finish line, ensuring they remain in a state of perpetual incompletion and cannot book a 'win'.

**Type:** `hybrid` · **Strategy:** **#6 Y Degradation** · `B(Y)↓ + C(Y)↑` · **Cluster:** C05 — Data Manipulation & Metric Engineering

**Cited principles:** Kahneman, Tversky, Arkes & Blumer, Arkes, Blumer

---

## Classification Rationale

**Ambiguity Source.** The phrase 'Definition of Done' is borrowed from Agile/Scrum software practice — a specific, named artifact in a specific delivery methodology. But the underlying move (changing the success criteria mid-flight to deny a rival their finish-line claim) is a generic 'moving the goalposts' pattern applicable wherever completion is socially adjudicated.

**Specific Interpretation.** In a delivery-organization context — engineering, product, transformation programs — the tactic operates by manipulating the codified completion artifact (Definition of Done, acceptance criteria, exit gates, KPIs) just before a rival's project crosses the line, ensuring the rival cannot ring the bell and book political credit for the milestone.

**Generic Interpretation.** A general influence pattern: any time an outcome's 'success' depends on satisfying criteria controlled by a third party, those criteria can be revised at the moment of imminent satisfaction to keep the actor in a perpetual not-yet-succeeded state. The mechanism does not require Agile, software, or even project work — only criterion ambiguity and adjudicator control.

**Primary Classification.** generic

**Reasoning.** While 'Definition of Done' is a specific Agile term, the operative mechanism — terminal-stage criteria revision — is a reusable pattern observable from PhD defenses to peace negotiations to acquisition closings. The Agile vocabulary is the costume; the underlying move is far older and broader. Generic primary because the mechanism is what travels.

---

## Specific Analysis

### Choice Architecture

- **Option X:** Rival's project remains in perpetual 'almost done' state, unable to book a clean completion win
- **Option Y:** Rival's project crosses the Definition of Done line and the rival publicly claims the milestone, the credit, and the political capital that follows
- **Context:** A delivery organization (engineering, product, or transformation program) where a rival leader is approaching a high-visibility milestone, and the attacker — usually a peer with adjacent authority over the acceptance criteria, gate review, or KPI definition — can introduce new conditions, edge cases, or quality bars at the eleventh hour.

### Active Levers

#### B(X)↑ — Amplify benefit of X — Not active

The tactic does not make incompletion intrinsically more attractive to the rival — no one prefers a stalled project. The attacker is not selling X to the rival; the attacker is simply preventing Y from being credited. The mechanism operates entirely on Y's side of the ledger.

#### C(X)↓ — Reduce cost of X — Not active

Continuing in perpetual incompletion is not made cheaper — in fact it grows more expensive over time as the rival burns more budget and credibility. The attacker is content with this; reducing the cost of X is not part of the mechanism.

#### B(Y)↓ — Diminish benefit of Y — **Active** · intensity 3 (Intense)

This is the central operating lever. Each time the rival approaches the bell, the criteria are revised so that the act of 'reaching the line' no longer constitutes a win. The political payoff of completion — the announcement, the kudos email, the executive recognition — is systematically severed from the engineering act. The rival can hit every criterion they were told to hit and still not be 'done.'

#### C(Y)↑ — Amplify cost of Y — **Active** · intensity 3 (Intense)

Every revision forces additional cycles of rework, testing, documentation, and stakeholder re-alignment. The cost of pursuing completion compounds: each near-finish becomes a sunk-cost trap that makes abandonment painful, but each new criterion makes the remaining work materially larger. Arkes & Blumer's sunk-cost effect locks the rival in even as the work expands.

### Strategy

**#6 Y Degradation** · `B(Y)↓ + C(Y)↑`

**Rationale.** The tactic operates exclusively on the alternative's side of the ledger — making completion both materially harder (more work) and politically worthless (criteria moved, so 'done' is never 'done enough'). It is inverse-asymmetric: the attacker offers no positive alternative path; they simply ensure the rival's chosen path never quite arrives. The result is a perpetual treadmill where effort never converts into recognized achievement.

**Effectiveness factors.** Requires the attacker to have either authority over or significant input into the acceptance artifact — product owner, QA lead, governance committee chair, executive sponsor. Requires plausible justifications for each revision ('the customer just surfaced this requirement,' 'compliance updated their guidance,' 'we learned this in the last review'). Fails when criteria are externally locked (contract, regulator, fixed-scope SOW) or when an executive sponsor protects the rival's gate and freezes the definition. Also fails if the rival publicly documents each criteria change with timestamps — the visible pattern becomes evidence of bad faith.

---

## Generic Analysis

### Influence Mechanism

**Psychological Principle.** Sunk-Cost Effect (Arkes & Blumer, 1985) combined with Goalpost-Shifting / Moving Reference Point (Kahneman & Tversky's Prospect Theory): the target's reference point for 'success' is repeatedly relocated by the criterion-holder, so each prior investment becomes a loss-domain commitment to keep pushing toward an ever-receding finish, even as the marginal value of completion is being eroded by the same revisions.

**Decision Alteration.** Transforms the target's choice from 'complete the work, get the win' into 'keep paying to chase a receding line, or accept a visible loss by abandoning.' Because each round of effort is sunk and each new criterion is framed as 'just one more thing,' the target rationally continues — but the criterion-holder controls when (or whether) the bell can be rung. The decision becomes adjudication-bounded rather than effort-bounded.

**Optimal Conditions.** Works best where completion criteria are subjective or codified in a document the attacker can edit, where the adjudicator has continuous (not one-shot) authority, where the target has high sunk costs, and where the broader audience does not closely track criterion-change history. Fails when criteria are externally fixed, sunk costs are low (target can walk away cheaply), or the audience explicitly tracks goalpost history.

### Representative Scenario 1

**Context:** Doctoral candidate in a life sciences lab whose advisor controls the 'ready to defend' judgment, and who is reluctant to lose a productive senior student because their departure means restarting the project pipeline.

**Sample X:** PhD candidate remains 'almost finished' for a fifth and sixth year while advisor keeps adding required experiments

**Sample Y:** Candidate defends, files, and walks across the stage as Dr.

**Template levers:**

- B(X)↑ ✗ — Lingering as an ABD candidate is not made more attractive — it is simply the residual state when defense is denied.

- C(X)↓ ✗ — Stipend support, lab access, and identity-as-grad-student persist, but these are pre-existing conditions, not benefits the tactic creates.

- B(Y)↓ ✓ — Each time the candidate approaches a defendable thesis, the advisor frames the current body of work as 'almost there but not quite a complete story yet,' so the candidate's accumulated chapters no longer constitute a 'done' thesis.

- C(Y)↑ ✓ — Each new 'one more experiment' adds six to twelve months of bench work, additional publication requirements, and revised committee expectations — the cost of arriving at defense compounds with every revision.

### Representative Scenario 2

**Context:** M&A negotiation where a strategic acquirer has identified that the target's founders are running out of bridge financing, and the acquirer's deal team can use successive rounds of 'one more confirmatory request' to extend the timeline until the target accepts a renegotiated lower price (or the deal collapses to the acquirer's strategic advantage).

**Sample X:** Acquisition target firm remains 'in due diligence' indefinitely while acquirer keeps surfacing new disclosure requirements

**Sample Y:** Deal closes, target's shareholders are paid, founders cash out

**Template levers:**

- B(X)↑ ✗ — Remaining in extended diligence offers no benefit to the target — they are bleeding cash and management attention with each passing week.

- C(X)↓ ✗ — The cost of remaining in diligence-purgatory actually rises over time as runway shortens; the tactic does not relieve this.

- B(Y)↓ ✓ — Even when the target satisfies every information request, the acquirer reframes the package as incomplete, so 'closing' as previously defined no longer counts — the target hits the line and the line moves.

- C(Y)↑ ✓ — Each new disclosure round triggers fresh legal, accounting, and management bandwidth costs; the target's path to close gets materially more expensive even as the negotiating leverage erodes.

### Versatility

**Level:** high

**Explanation.** Applicable in any context where (a) 'success' is defined by criteria, (b) the criteria are at least partially under the influence of someone other than the actor pursuing them, and (c) the adjudicator's authority is continuous rather than one-shot. Includes corporate project governance, academic credentialing, regulatory licensing, peace negotiations, sales pipeline gating, contract execution, M&A close, immigration adjudication, performance review cycles, and grant-funded research milestones. Less effective where criteria are fixed by an external authority (contract, statute, ISO standard) or where one-shot adjudication closes the goalpost-moving window.

### Core Strategy

**#6 Y Degradation** · `B(Y)↓ + C(Y)↑`

### Application Examples

- Corporate: A peer VP with quality-gate authority adds new acceptance criteria the night before a rival product launch, ensuring the rival's GA announcement slips out of the quarter and the credit lands on no one
- Academic: A dissertation advisor with unresolved tenure anxiety keeps adding 'just one more experiment' to a senior PhD's requirements, retaining the senior student's productivity by denying them their defense
- Government: A regulator processing a license application repeatedly issues 'requests for additional information' as the applicant approaches approval, allowing a politically preferred competitor to enter the market first
- Lobbying: A legislative committee chair adds new amendments to a bill at each markup just as proponents secure majority support, ensuring the bill never reaches a floor vote in its passable form
- Diplomacy: A negotiating party introduces fresh preconditions each time the counterparty has met the prior set, keeping the talks open without progress and burning the counterparty's political capital at home
- Sales: An enterprise buyer's procurement team adds new security review, legal review, and compliance review requirements each time the vendor satisfies the prior round, extending the cycle past the vendor's quarter-end and weakening the vendor's pricing position

---

## Integrated Insights

### Pattern Recognition

Both lenses converge on Y Degradation — the tactic's identity is fundamentally about preventing a rival's success, not promoting an alternative. This is what distinguishes it from the cluster sibling CRITERIA SHIFTING (0274), which operates more broadly across the full lifecycle (criteria can be shifted at proposal time, mid-execution, or at close). DEFINITION OF DONE WARFARE specifically targets the terminal moment — the bell-ringing — and weaponizes the artifact that defines completion. The cruelty (and effectiveness) lies in the timing: criteria are shifted precisely when the rival is positioned to declare victory, maximizing the sunk-cost trap and the emotional whiplash. The Agile-era vocabulary is also significant: where 'moving the goalposts' is recognizable as bad faith, 'updating the Definition of Done' is laundered through methodology-speak, giving the attacker plausible cover as a diligent practitioner.

### Strategic Implications

For the practitioner deploying the tactic: leverage requires controlling or co-authoring the acceptance artifact, plausible justifications for each revision, and an audience that does not closely track the history of criterion changes. The tactic has a self-limiting trajectory — sustain it too long and the pattern becomes visible, at which point credibility damage flips back onto the attacker. For the defender (the rival being targeted): the structural countermove is to lock criteria in writing before commencement, with explicit change-control language, and to maintain a dated changelog of every revision. The audience-side countermove is to elevate the gating decision to a sponsor with the political weight to freeze the definition. The contrast with GOLDEN HANDCUFFS (0018) is instructive — that tactic uses Strategy 9 (B(X)↑ + C(Y)↑) to retain dissenters with financial incentives plus exit costs; DEFINITION OF DONE WARFARE uses Strategy 6 (B(Y)↓ + C(Y)↑) to deny a rival's success without offering them any positive path.

### Resolution Approach

Use the specific lens when the discussion is about a particular delivery organization, an identifiable acceptance artifact (DoD, exit criteria, KPI scorecard), and a named rival's project. Use the generic lens when discussing the broader 'goalpost-shifting at the moment of imminent completion' pattern — particularly when comparing across domains (academic, regulatory, M&A) where the mechanism is identical but the vocabulary differs. The generic frame is more durable for cross-domain practitioner education; the specific frame is more actionable for someone currently inside a delivery organization watching this happen to a peer.

---

## Metadata

- **Tactic ID:** `0458`
- **Cluster:** `C05`
- **Source index:** 457
- **Theorists cited:** Kahneman, Tversky, Arkes & Blumer, Arkes, Blumer