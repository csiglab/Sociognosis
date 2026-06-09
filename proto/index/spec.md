# Index

> In this document we will create the specification for the entire index of the **Sociognosis** project.

> The **Sociognosis** aims to identify and formalize the set of epistemic elements that enable an agent to effectively navigate social reality (through understanding and action).

## Data Schema

See `../../docs/data/index/schema/schema.json`.

### Category

**Ontology and epistemology are the right hand and left hand of knowledge construction: they are mutually constraining duals of the same epistemic act.**

- **Ontology** = what *is* (constraint space of reality)
- **Epistemology** = how it is *accessed/represented* (constraint space of knowing)
- They are not separate domains, but **co-dependent operators on the same reality-model interface**


Scaffold Status: Indicates whether the element functions as an epistemic scaffold for the construction, guidance, validation, organization, or operation of epistemic artifacts and processes.  

- **Scaffold: :** Directly or indirectly supports, structures, constrains, guides, enables, coordinates, validates, or organizes epistemic activity. Its primary role is to assist the production, management, evaluation, communication, or use of knowledge.
- **Non-Scaffold:** Does not perform a scaffolding function; instead serves as an object, target, output, agent, or product of epistemic activity.

| **Category** | **Description** | **Instance(s)** | **Scaffold Status** |
| --- | --- | --- | --- |
| **Epistemic Purpose** | The telos or intended epistemic objective that motivates the activity. Defines *why* knowledge is being produced. | Explanation, prediction, control, diagnosis, discovery, description, forecasting, intervention, understanding | Scaffold |
| **Reality** | The ontological substrate comprising the actual states, structures, processes, entities, and causal dynamics that exist independently (or partially independently) of any observer’s representation. Reality constitutes the ultimate source domain from which observations are extracted, against which epistemic artifacts are validated, and whose structure constrains possible knowledge. It includes both observable and unobservable phenomena, latent mechanisms, causal architectures, and state trajectories across time. | Physical systems, biological organisms, chemical reactions, social institutions, computational systems, economic systems, ecological networks, latent variables, hidden causal mechanisms, dynamical state spaces, material processes, environmental structures. | Non-Scaffold |
| Realty Section (Epistemic Object Set) | … | … | Non-Scaffold |
| **Observation Interface** | The sensorimotor boundary + inscription process that transduces a Domain Snapshot into a persistent encoded artifact. Includes transduction, sampling, quantization, encoding, and storage. | CMOS sensor + ADC + JPEG + SD card; thermocouple + data logger + CSV file; human retina + V1 cortex + working memory. | Scaffold |
| **Observation Encoding** |  |  | Scaffold |
| **Epistemic Representation Form (Epistemic Blueprint)** | Encoding format or substrate in which artifacts are expressed; constrains manipulation and interpretation. | Directed Acyclic Graph (DAG), Structural Equation (functional notation), Polynomial Equation, … | Scaffold |
| **Concrete Epistemic Artifact** | Structured object and **specific object** that encodes claims, constraints, or distributions over reality; the primary carrier of semantic content. | ***Zero free parameters**** – every coefficient, distribution, variable, and functional form is concretely specified. | Yes – can be evaluated as correct/incorrect against reality. | `y = 2.3x + 1.7` (fitted linear model); specific CSV file `[2.1, 3.4, 5.6]`; a particular DAG with all edges and functional forms fixed. - Propositions, numbers, datasets, differential equations, probabilistic models, Hypergraphs, property encoding, | Non-Scaffold |
| **Domain Concrete Epistemic  Artifact Set  (DCESA)** | The complete collection of instantiated epistemic objects produced and used to describe, explain, predict, and manipulate a specific domain of reality. | … | Non-Scaffold |
| **Epistemic Gap** | Portion of reality for which no adequate artifact, model, observation, or explanatory structure currently exists. | … | Scaffold |
| **Epistemic Agent** | Entity that performs epistemic operations by applying tools to artifacts. | Scientist, analyst, research institution, machine learning system, automated pipeline | Non-Scaffold |
| **Epistemic Goal Set** | The collection of specific desired epistemic outcomes that guide inquiry, observation, modeling, validation, and reasoning within a given epistemic process. Goals define the target knowledge state that an agent seeks to reach regarding a reality section. | Identify causal mechanisms; estimate parameter values; discover latent variables; classify entities; predict future states; explain observed phenomena; reduce uncertainty; detect anomalies; estimate risk; construct taxonomies; infer hidden states; evaluate interventions; improve forecast accuracy; characterize system structure; determine boundary conditions; identify governing laws; measure quantities; validate hypotheses; generate new hypotheses; optimize model performance. |  |
| **Epistemic Process (Activity)** | Ordered sequence of tool applications over time; defines the dynamics of knowledge construction. | Scientific method, Bayesian updating loop, training pipeline, experimental cycle |  |
| **Epistemic Standard** | Normative criteria used to evaluate validity, correctness, or acceptability of artifacts and processes. | Logical consistency, statistical significance, reproducibility, robustness, falsifiability |  |
| **Encoding Substrate** | An encoding substrate is the medium in which information is physically instantiated. | Paper,  Ink,  Electromagnetic Signal, … |  |
| **Epistemic Domain (Target Domain)**  | Segment of reality that the epistemic practice targets or models. | Physical systems, biological systems, social systems, computational systems |  |
| **Epistemic Constraint** | Limitation that bounds what can be known or inferred within the system. | Noise, limited data, computational complexity, identifiability issues, measurement error, ignorance, intractability, stochasticity, higher-order stochasticity, chaos, nonlinearity, uncertainty propagation, and observational limitations. |  |
| **Epistemic Infrastructure** | Supporting environment that enables storage, computation, measurement, and communication of artifacts. | Sensors, laboratories, software systems, databases, notebooks, scientific publications |  |
| **Epistemic Feedback** | Signal from reality (or from another artifact) that resists or confirms prior predictions or actions; primary driver of learning and error correction. | Prediction error (residual), unexpected observation, failed intervention, successful replication, sensor saturation, model divergence, comparison between two Domain Snapshots taken at different times. |  |
| **Epistemic Act** | Primitive, non‑decomposable operation performed by an agent: attending, discriminating, remembering, anticipating, intervening, comparing, observing (which invokes Observation Encoding). | Attending to a sensor reading, detecting a difference, recalling an observation, emitting a prediction, pressing a measurement probe, judging similarity, encoding a raw signal into a digital value. |  |
| **Epistemic Principle** | Foundational normative, structural, or strategic rule that governs how epistemic agents should construct, validate, organize, or revise knowledge. Principles shape the selection of standards, tools, and processes by defining the underlying logic of inquiry. | Empiricism, falsifiability, parsimony (Occam’s Razor), Bayesian coherence, causal reasoning, reproducibility, predictive adequacy, reductionism, systems thinking, explanatory power, measurement invariance |  |
| **Epistemic Prior (Inductive Bias)** | Pre-existing assumptions, expectations, structural preferences, or probability distributions that constrain hypothesis generation and inference before new evidence is incorporated. Priors determine what explanations are considered plausible and influence search trajectories through hypothesis space. | Gaussian prior,  Simplicity preference, Smoothness assumption, Locality assumption |  |
| **Epistemic Strategy** | Adaptive, context-dependent planning logic that governs how epistemic agents allocate resources, sequence inquiry, navigate uncertainty, and select investigative pathways to achieve epistemic objectives under real-world constraints. Strategies operationalize principles into executable inquiry architectures by determining search order, decomposition methods, validation sequencing, exploration/exploitation balance, and intervention priorities. | Exploratory data analysis before formal modeling; hypothesis-first experimentation; reductionist decomposition; systems-level integrative analysis; sequential Bayesian updating; active learning; robustness-first validation; coarse-to-fine modeling; simulation-before-deployment; high-throughput screening; falsification-driven testing; divide-and-conquer investigation; iterative refinement; uncertainty minimization; adversarial stress testing; hierarchical model building. |  |
| **Epistemic Framework** | Abstract conceptual, inferential, and formal systems that structure how epistemic agents interpret observations, organize knowledge, generate explanations, and reason about reality. Frameworks define the overarching cognitive architecture within which principles, operators, and artifacts are selected and deployed. | Logic, causal inference, Bayesian reasoning, statistical reasoning, systems theory, cybernetics, information theory, mechanistic modeling, optimization theory, game theory, control theory, reductionist frameworks, complexity science, decision theory |  |
| **Epistemic Operator** | Formal or procedural mechanism used to construct, transform, representation form ( abstract artifact)or validate epistemic artifacts. | Algebraic manipulation, statistical inference, optimization algorithms, simulation methods, measurement procedures,  generic or abstract class of artifact or let’s called it by representational form. |  |

#### Reality

> (Ontology)

> Use this for the specific of ontic nodes.

| **Layer** | **Category** | **Type** | **Description** | **Instance(s)** | **Tag(s)** |
| --- | --- | --- | --- | --- | --- |
| **Ontic** | **Existential** | Substantive | Self-identical existents with bounded persistence | Hydrogen atom; Redwood tree; Blockchain node | `matter` `object` `agent` `bearer-of-properties` |
|  |  | Processual | Dynamic occurrences extended in time | Photosynthesis; Tectonic drift; Radioactive decay | `becoming` `event` `flux` `transformation` |
|  |  | Entity | Conceptual or ontological units treated as “things” in modeling | Person; Corporation; Planet | `object` `unit` `system-component` |
|  |  | Mechanism | Structures or interactions that generate or regulate processes | Enzyme complex; Gear train; Feedback loop | `mechanism` `causal-structure` `function` |
|  | **Dynamical** |  |  |  |  |
|  |  | Event | Discrete, delimited change or occurrence marking a transition between states. | Collision; Birth; System crash; Market shock | `event` `transition` `punctual` `change` |
|  |  | Process | Temporally extended, **causally connected** sequence of events generating a state-trajectory. | Erosion; Learning; Metabolism; Capital accumulation | `process` `trajectory` `causal-sequence` `temporal-extension` |
|  |  | Stochastic | Dynamics governed by probabilistic laws rather than deterministic evolution; outcomes defined over distributions. | Brownian motion; Mutation; Packet loss; Default risk | `probabilistic` `random-variable` `distribution` `uncertainty` |
|  |  | **Event Stream** | A very general construct to capture the generated **‘Manifestations’** by a given piece of reality (system, process, etc).  |  |  |
|  |  | **Mixture Event Stream** | A **superposition or composition of multiple event-generating processes**, where the observed stream is generated by a latent mixture (e.g., competing or interacting sources). | … | `mixture` `superposition` `latent-source` `aggregation` |
|  |  | Phenomena | A **higher-order property of a state-trajectory**, i.e. a pattern or regularity predicated over a sequence of states generated by one or more processes. | Inflation, Diffusion, Skill Decay | `pattern` `regularity` `macro-effect` `trajectory-level` |
|  |  | Epiphenomena 💨 | Secondary or byproduct phenomena that arise from primary processes or structures but **do not influence those processes themselves**. They are consequences, not causes. | Heat from computation; Exhaust noise; UI lag shimmer | `byproduct` `non-causal` `derivative` |
|  | **Agency** | **Agent** |  |  |  |
|  |  | **Intention (Goal)** |  |  |  |
|  | Substance 🧱 |  | Entities that exist independently and underpin properties or processes. |  |  |
|  |  |  |  |  |  |
| **Synontic** | **Structural** | Self-organizing | Emergent order from local interactions | Termite mounds; Neural networks; Supply chains | `emergence` `pattern` `organization` `collective` |
|  | **Structural** | Institutional | Stabilized constraints on behavior | Legal systems; Grammar; Market protocols | `convention` `norm` `stabilization` `scaffold` |
|  |  | Rhizome | … | … | … |
|  | **Emergence** | .. | .. | .. | … |
|  | **Relation** | Causal | Productive dependencies between existents | Force transmission; Gene regulation; Influence networks | `causation` `production` `determination` `flow` |
|  | **Relation** | Significant | Meaning-laden connections via interpretation | Semiotic chains; Cultural associations; Semantic web | `meaning` `reference` `aboutness` `intentionality` |
|  | **Protocol** | Coordination | Rules enabling collective alignment | Language syntax; TCP/IP; Diplomatic etiquette | `alignment` `communication` `interface` `standard` |
|  | **Affordance** | Action-potential | Environmental features soliciting engagement | Door-handle graspability; Display clickability; Trail following | `invitation` `engagement` `solicitation` `pragmatic` |
|  | Space 📏 | The framework of coexistence and positional structure among entities. |  |  |  |
|  | Time ⏳ | The ordering of events and transformations along a temporal dimension. |  |  |  |
|  | Environment 🌿 |  | External influences and conditions that affect a system or field without being part of it. |  |  |
|  | **Substrate** |  |  |  |  |
|  | Property |  |  |  |  |
|  | Aspect |  |  |  |  |
|  | Variable Aspect |  |  |  |  |
|  | **State** | Configurational | Temporal arrangement of components | Crystal lattice; Biological homeostasis; Thermodynamic equilibrium | `arrangement` `condition` `momentary` `snapshot` |
| Meta Ontic |  |  |  |  |  |
|  |  | Information |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |