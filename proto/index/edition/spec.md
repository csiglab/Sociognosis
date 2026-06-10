
# Spec

> Let's create a mechanism to edit the file  `../../docs/data/index/data.json` - that follows this schema  `../../docs/data/index/schema/schema.json`.

> This is part of - The **Sociognosis** aims to identify and formalize the set of epistemic elements that enable an agent to effectively navigate social reality (through understanding and action).

Features:

1. Show a `graph - force layout` - allow the search of the nodes - and simple edit - like adding links between the nodes.
2. Add a side panel that allow the full edit - including adding links.
3. Allow to save the new data.json
4. Alow to add new nodes - both in json - and using the form - to fill the fields.
5. Make sures that the dropdowns - if are always searcable.
6. Use the data in the JSON file to facilitate the completion of the remaining fields in the same file.

## Data Schema

See `../../docs/data/index/schema/schema.json`.

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/product-space-node.schema.json",
  "title": "Sociognosis Index Node Schema",
  "description": "A formal ontic-epistemic schema underlying the structure of understanding and agency in social reality.",
  "type": "object",
  "required": [
    "id",
    "name",
    "category",
    "inheritanceLevel",
    "description",
    "functionalRoles",
    "domainScope",
    "historicalContext",
    "specific",
    "relationships",
    "metadata",
    "references"
  ],
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "category": {
      "type": "string",
      "description": "Category of the entity in the ontic epistemic schema for Sociognosis.",
      "enum": [
        "Epistemic Purpose",
        "Reality",
        "Observation Interface",
        "Observation Encoding",
        "Epistemic Representation Form (Epistemic Blueprint)",
        "Concrete Epistemic Artifact",
        "Epistemic Gap",
        "Epistemic Agent",
        "Epistemic Goal",
        "Epistemic Process (Activity)",
        "Epistemic Standard",
        "Encoding Substrate",
        "Epistemic Domain (Target Domain)",
        "Epistemic Constraint",
        "Epistemic Infrastructure",
        "Epistemic Feedback",
        "Epistemic Act",
        "Epistemic Principle",
        "Epistemic Prior (Inductive Bias)",
        "Epistemic Strategy",
        "Epistemic Framework",
        "Epistemic Operator"
      ]
    },
    "inheritanceLevel": {
      "type": "integer",
      "minimum": 0
    },
    "description": {
      "type": "string"
    },
    "longDescription": {
      "type": "string"
    },
    "functionalRoles": {
      "type": "array",
      "description": "The set of roles that the node (entity) plays in our epistemic efforts to capture a section of reality, analogous to the Scaffold Status.",
      "items": {
        "type": "string"
      }
    },
    "domainScope": {
      "type": "array",
      "description": "Economic, industrial, or production domains where the node operates",
      "items": {
        "type": "string"
      }
    },
    "historicalContext": {
      "type": "object",
      "required": [
        "summary",
        "chronology"
      ],
      "properties": {
        "summary": {
          "type": "string"
        },
        "chronology": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "year",
              "event",
              "context"
            ],
            "properties": {
              "year": {
                "type": "number"
              },
              "event": {
                "type": "string"
              },
              "context": {
                "type": "string"
              }
            }
          }
        }
      }
    },
    "specific": {
      "type": "object",
      "description": "Category-specific structured extension fields"
    },
    "relationships": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "relationshipType",
          "targetNodeId",
          "description"
        ],
        "properties": {
          "relationshipFamily": {
            "type": "string",
            "enum": [
              "FUNCTIONAL",
              "STRUCTURAL",
              "CAPABILITY_DEPENDENCY",
              "VALUE_CHAIN",
              "MARKET_RELATION",
              "GOVERNANCE",
              "TEMPORAL_EVOLUTION",
              "COMPOSITIONAL",
              "CLASSIFICATION"
            ]
          },
          "relationshipType": {
            "type": "string",
            "enum": [
              "PRODUCES",
              "CONSUMES",
              "ENABLES",
              "REQUIRES",
              "DEPENDS_ON",
              "PART_OF",
              "TRANSFORMS_INTO",
              "SPECIALIZES",
              "GENERALIZES",
              "COMPLIES_WITH",
              "CONSTRAINED_BY",
              "COMPETES_WITH",
              "SUBSTITUTES_FOR",
              "COMPLEMENTS",
              "ORCHESTRATED_BY",
              "EVOLVES_FROM",
              "SUPERSEDES"
            ]
          },
          "targetNodeId": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "required": [
        "tags",
        "confidenceScore",
        "sourceReference",
        "createdAt",
        "auditTrail"
      ],
      "properties": {
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "confidenceScore": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "sourceReference": {
          "type": "string"
        },
        "createdAt": {
          "type": "string",
          "format": "date-time"
        },
        "auditTrail": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "reviewDate",
              "reviewNote"
            ],
            "properties": {
              "reviewDate": {
                "type": "string",
                "format": "date"
              },
              "reviewNote": {
                "type": "string"
              }
            }
          }
        }
      }
    },
    "references": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "title",
          "description"
        ],
        "properties": {
          "title": {
            "type": "string"
          },
          "link": {
            "type": "string",
            "format": "uri"
          },
          "description": {
            "type": "string"
          }
        }
      }
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Purpose"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicPurposeSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Reality"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/RealitySpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Observation Interface"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/ObservationInterfaceSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Observation Encoding"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/ObservationEncodingSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Representation Form (Epistemic Blueprint)"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicRepresentationFormSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Concrete Epistemic Artifact"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/ConcreteEpistemicArtifactSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Gap"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicGapSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Agent"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicAgentSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Goal"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicGoalSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Process (Activity)"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicProcessSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Standard"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicStandardSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Encoding Substrate"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EncodingSubstrateSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Domain (Target Domain)"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicDomainSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Constraint"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicConstraintSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Infrastructure"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicInfrastructureSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Feedback"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicFeedbackSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Act"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicActSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Principle"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicPrincipleSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Prior (Inductive Bias)"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicPriorSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Strategy"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicStrategySpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Framework"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicFrameworkSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "Epistemic Operator"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/EpistemicOperatorSpecific"
          }
        }
      }
    }
  ],
  "$defs": {
    "EpistemicPurposeSpecific": {
      "type": "object",
      "required": ["purposeType"],
      "properties": {
        "purposeType": {
          "type": "string",
          "description": "The telos or intended epistemic objective.",
          "enum": [
            "explanation",
            "prediction",
            "control",
            "diagnosis",
            "discovery",
            "description",
            "forecasting",
            "intervention",
            "understanding",
            "other"
          ]
        },
        "intendedOutcome": {
          "type": "string",
          "description": "Free-text description of what the knowledge is supposed to achieve."
        }
      }
    },
    "RealitySpecific": {
      "type": "object",
      "required": ["onticLayer", "onticCategory"],
      "properties": {
        "onticLayer": {
          "type": "string",
          "description": "The primary layer of reality according to the ontic schema.",
          "enum": ["Ontic", "Synontic", "MetaOntic"]
        },
        "onticCategory": {
          "type": "string",
          "description": "The specific ontic kind, drawing from the ontology template.",
          "enum": [
            "Substantive",
            "Processual",
            "Entity",
            "Mechanism",
            "Event",
            "Process",
            "Stochastic",
            "EventStream",
            "MixtureEventStream",
            "Phenomena",
            "Epiphenomena",
            "Agent",
            "Goal",
            "SelfOrganizing",
            "Institutional",
            "Rhizome",
            "CausalRelation",
            "SignificantRelation",
            "CoordinationProtocol",
            "Affordance",
            "Space",
            "Time",
            "Environment",
            "Substrate",
            "Property",
            "Aspect",
            "VariableAspect",
            "State",
            "Information"
          ]
        },
        "realityDescription": {
          "type": "string",
          "description": "Summary of the specific segment of reality being referenced."
        },
        "latentStructures": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Hidden or unobserved mechanisms thought to underlie the phenomena."
        }
      }
    },
    "ObservationInterfaceSpecific": {
      "type": "object",
      "required": ["transductionMethod", "encodingFormat"],
      "properties": {
        "transductionMethod": {
          "type": "string",
          "description": "How raw phenomena are converted into a signal (e.g., CMOS sensor, thermocouple, human retina)."
        },
        "samplingStrategy": {
          "type": "string",
          "description": "How continuous reality is sampled (e.g., periodic, event-triggered)."
        },
        "quantization": {
          "type": "string",
          "description": "Quantization scheme (e.g., 8-bit ADC, categorical bins)."
        },
        "encodingFormat": {
          "type": "string",
          "description": "Format of the initial encoded observation (e.g., JPEG, CSV, neural spike train)."
        },
        "storageMedium": {
          "type": "string",
          "description": "Where the encoded observation is first stored (e.g., SD card, working memory)."
        }
      }
    },
    "ObservationEncodingSpecific": {
      "type": "object",
      "required": ["encodingStandard"],
      "properties": {
        "encodingStandard": {
          "type": "string",
          "description": "Formal or conventional standard for the encoded data (e.g., MIME type, file format, neural code)."
        },
        "resolution": {
          "type": "string",
          "description": "Spatial/temporal/intensity resolution of the encoding."
        },
        "compression": {
          "type": "string",
          "description": "Whether lossy or lossless compression is used."
        }
      }
    },
    "EpistemicRepresentationFormSpecific": {
      "type": "object",
      "required": ["formType"],
      "properties": {
        "formType": {
          "type": "string",
          "description": "The abstract representational genus (e.g., DAG, structural equation, graph, polynomial).",
          "enum": [
            "DirectedAcyclicGraph",
            "StructuralEquation",
            "PolynomialEquation",
            "DifferentialEquation",
            "BayesianNetwork",
            "Matrix",
            "Hypergraph",
            "LogicalFormula",
            "DecisionTree",
            "NeuralNetworkArchitecture",
            "other"
          ]
        },
        "formalSystem": {
          "type": "string",
          "description": "The mathematical or logical system that governs the form (e.g., algebra, predicate logic, probability theory)."
        },
        "expressiveness": {
          "type": "string",
          "description": "What class of relations or functions the form can capture (e.g., linear, non-linear, cyclic)."
        }
      }
    },
    "ConcreteEpistemicArtifactSpecific": {
      "type": "object",
      "required": ["artifactType", "encodingFormat"],
      "properties": {
        "artifactType": {
          "type": "string",
          "description": "Concrete kind of artifact (e.g., fitted model, dataset, specific equation, simulation run).",
          "enum": ["equation", "dataset", "model", "graph", "table", "text", "code", "image", "other"]
        },
        "encodingFormat": {
          "type": "string",
          "description": "Syntax or serialization (e.g., CSV, JSON, Python code, LaTeX)."
        },
        "verificationStatus": {
          "type": "string",
          "enum": ["unverified", "verified", "falsified", "underReview"]
        },
        "artifactHash": {
          "type": "string",
          "description": "Content hash for identity and integrity."
        }
      }
    },
    "EpistemicGapSpecific": {
      "type": "object",
      "required": ["gapDescription"],
      "properties": {
        "gapDescription": {
          "type": "string",
          "description": "What is unknown or inadequately modeled."
        },
        "scope": {
          "type": "string",
          "description": "Boundaries of the gap (e.g., spatial, temporal, conceptual)."
        },
        "urgency": {
          "type": "string",
          "enum": ["low", "medium", "high", "critical"]
        },
        "researchQuestions": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "EpistemicAgentSpecific": {
      "type": "object",
      "required": ["agentType"],
      "properties": {
        "agentType": {
          "type": "string",
          "enum": ["individualHuman", "researchTeam", "institution", "automatedSystem", "AI", "other"]
        },
        "capabilities": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Specific cognitive or computational capabilities."
        },
        "domainExpertise": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "EpistemicGoalSpecific": {
      "type": "object",
      "required": ["goalType"],
      "properties": {
        "goalType": {
          "type": "string",
          "description": "The epistemic outcome the goal aims for.",
          "enum": [
            "identifyCausalMechanisms",
            "estimateParameters",
            "discoverLatentVariables",
            "classifyEntities",
            "predictFutureStates",
            "explainObservedPhenomena",
            "reduceUncertainty",
            "detectAnomalies",
            "estimateRisk",
            "constructTaxonomies",
            "inferHiddenStates",
            "evaluateInterventions",
            "improveForecastAccuracy",
            "characterizeSystemStructure",
            "determineBoundaryConditions",
            "identifyGoverningLaws",
            "measureQuantities",
            "validateHypotheses",
            "generateHypotheses",
            "optimizeModelPerformance",
            "other"
          ]
        },
        "priority": {
          "type": "string",
          "enum": ["primary", "secondary", "background"]
        },
        "targetRealitySection": {
          "type": "string",
          "description": "Reference to the reality segment the goal addresses."
        }
      }
    },
    "EpistemicProcessSpecific": {
      "type": "object",
      "required": ["processType"],
      "properties": {
        "processType": {
          "type": "string",
          "enum": [
            "scientificMethod",
            "bayesianUpdating",
            "trainingPipeline",
            "experimentalCycle",
            "simulationStudy",
            "literatureReview",
            "modelComparison",
            "dataCollection",
            "other"
          ]
        },
        "steps": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Sequence of activities or phases."
        },
        "toolDependencies": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "EpistemicStandardSpecific": {
      "type": "object",
      "required": ["standardType"],
      "properties": {
        "standardType": {
          "type": "string",
          "enum": [
            "logicalConsistency",
            "statisticalSignificance",
            "reproducibility",
            "robustness",
            "falsifiability",
            "predictiveAccuracy",
            "explanatoryPower",
            "parsimony",
            "other"
          ]
        },
        "threshold": {
          "type": "string",
          "description": "Quantitative or qualitative threshold (e.g., p<0.05)."
        },
        "appliedTo": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Types of artifacts or processes this standard evaluates."
        }
      }
    },
    "EncodingSubstrateSpecific": {
      "type": "object",
      "required": ["substrateType"],
      "properties": {
        "substrateType": {
          "type": "string",
          "enum": ["paper", "ink", "electromagneticSignal", "siliconMemory", "biologicalTissue", "other"]
        },
        "physicalProperties": {
          "type": "string",
          "description": "Key physical characteristics (e.g., magnetic coercivity, optical contrast)."
        }
      }
    },
    "EpistemicDomainSpecific": {
      "type": "object",
      "required": ["domainType"],
      "properties": {
        "domainType": {
          "type": "string",
          "description": "The broad area of reality targeted.",
          "enum": [
            "physicalSystem",
            "biologicalSystem",
            "socialSystem",
            "computationalSystem",
            "economicSystem",
            "ecologicalSystem",
            "cognitiveSystem",
            "other"
          ]
        },
        "scopeDescription": {
          "type": "string"
        }
      }
    },
    "EpistemicConstraintSpecific": {
      "type": "object",
      "required": ["constraintType"],
      "properties": {
        "constraintType": {
          "type": "string",
          "enum": [
            "noise",
            "limitedData",
            "computationalComplexity",
            "identifiabilityIssue",
            "measurementError",
            "ignorance",
            "intractability",
            "stochasticity",
            "higherOrderStochasticity",
            "chaos",
            "nonlinearity",
            "uncertaintyPropagation",
            "observationalLimitation",
            "other"
          ]
        },
        "impactDescription": {
          "type": "string"
        },
        "mitigationStrategies": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "EpistemicInfrastructureSpecific": {
      "type": "object",
      "required": ["infrastructureType"],
      "properties": {
        "infrastructureType": {
          "type": "string",
          "enum": [
            "sensor",
            "laboratory",
            "softwareSystem",
            "database",
            "computationalCluster",
            "publicationVenue",
            "repository",
            "other"
          ]
        },
        "components": {
          "type": "array",
          "items": { "type": "string" }
        },
        "accessibility": {
          "type": "string",
          "enum": ["open", "restricted", "proprietary"]
        }
      }
    },
    "EpistemicFeedbackSpecific": {
      "type": "object",
      "required": ["feedbackType"],
      "properties": {
        "feedbackType": {
          "type": "string",
          "enum": [
            "predictionError",
            "unexpectedObservation",
            "failedIntervention",
            "successfulReplication",
            "sensorSaturation",
            "modelDivergence",
            "comparisonSnapshot",
            "other"
          ]
        },
        "source": {
          "type": "string",
          "description": "Which artifact or reality segment generated the feedback."
        },
        "magnitude": {
          "type": "string",
          "description": "Strength or significance of the feedback signal."
        }
      }
    },
    "EpistemicActSpecific": {
      "type": "object",
      "required": ["actType"],
      "properties": {
        "actType": {
          "type": "string",
          "enum": [
            "attending",
            "discriminating",
            "remembering",
            "anticipating",
            "intervening",
            "comparing",
            "observing",
            "encoding",
            "other"
          ]
        },
        "agentRole": {
          "type": "string",
          "description": "How the agent is involved (e.g., human, automated)."
        }
      }
    },
    "EpistemicPrincipleSpecific": {
      "type": "object",
      "required": ["principleName"],
      "properties": {
        "principleName": {
          "type": "string",
          "description": "Name of the principle (e.g., Empiricism, Falsifiability, Parsimony)."
        },
        "description": {
          "type": "string"
        },
        "appliedTo": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Aspects of inquiry where the principle is applied (e.g., hypothesis generation, model selection)."
        }
      }
    },
    "EpistemicPriorSpecific": {
      "type": "object",
      "required": ["priorType"],
      "properties": {
        "priorType": {
          "type": "string",
          "enum": [
            "gaussianPrior",
            "simplicityPreference",
            "smoothnessAssumption",
            "localityAssumption",
            "sparsityPrior",
            "causalOrdering",
            "other"
          ]
        },
        "distribution": {
          "type": "string",
          "description": "If probabilistic, the specific distribution (e.g., Normal(0,1))."
        },
        "strength": {
          "type": "string",
          "description": "How strongly the prior influences inference."
        }
      }
    },
    "EpistemicStrategySpecific": {
      "type": "object",
      "required": ["strategyName"],
      "properties": {
        "strategyName": {
          "type": "string",
          "description": "Descriptive name of the strategy (e.g., ExploratoryDataAnalysis, ActiveLearning)."
        },
        "phase": {
          "type": "string",
          "enum": ["exploration", "validation", "exploitation", "refinement"]
        },
        "resourceAllocation": {
          "type": "string",
          "description": "How resources are allocated (e.g., compute, time, attention)."
        }
      }
    },
    "EpistemicFrameworkSpecific": {
      "type": "object",
      "required": ["frameworkName"],
      "properties": {
        "frameworkName": {
          "type": "string",
          "enum": [
            "logic",
            "causalInference",
            "bayesianReasoning",
            "statisticalReasoning",
            "systemsTheory",
            "cybernetics",
            "informationTheory",
            "mechanisticModeling",
            "optimizationTheory",
            "gameTheory",
            "controlTheory",
            "reductionism",
            "complexityScience",
            "decisionTheory",
            "other"
          ]
        },
        "underlyingPrinciples": {
          "type": "array",
          "items": { "type": "string" }
        },
        "applicability": {
          "type": "string"
        }
      }
    },
    "EpistemicOperatorSpecific": {
      "type": "object",
      "required": ["operatorType"],
      "properties": {
        "operatorType": {
          "type": "string",
          "enum": [
            "algebraicManipulation",
            "statisticalInference",
            "optimization",
            "simulation",
            "measurementProcedure",
            "dataTransformation",
            "graphAlgorithm",
            "other"
          ]
        },
        "inputs": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Kinds of artifacts or data the operator consumes."
        },
        "outputs": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Kinds of artifacts the operator produces."
        }
      }
    }
  },
  "additionalProperties": false
}

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


## Sample Data

[
	  {
    "id": "reality.market",
    "name": "Market",
    "category": "Reality",
    "inheritanceLevel": 2,
    "description": "A socially constituted institutional structure that coordinates voluntary exchange among economic agents through mechanisms of price formation, allocation, competition, and contractual interaction.",
    "longDescription": "A market is a synontic institutional configuration composed of agents, exchange protocols, property rights, contractual rules, information flows, and allocation mechanisms. Markets facilitate the discovery of prices, coordinate decentralized economic activity, transmit information regarding relative scarcity, and enable the exchange of goods, services, assets, labor, and other economic objects. Markets are emergent social structures sustained through repeated participation, legal enforcement, norms, and shared expectations. They are neither individual transactions nor specific organizations, but institutional environments within which such activities occur.",
    "functionalRoles": [
      "Resource Allocation",
      "Price Discovery",
      "Information Transmission",
      "Exchange Coordination",
      "Incentive Generation",
      "Competition Facilitation",
      "Economic Coordination"
    ],
    "domainScope": [
      "Economics",
      "Political Economy",
      "Industrial Organization",
      "International Trade",
      "Financial Systems",
      "Labor Systems"
    ],
    "historicalContext": {
      "summary": "Markets have existed in various forms throughout human history, ranging from local barter arrangements to highly complex global financial and digital marketplaces.",
      "chronology": [
        {
          "year": -3000,
          "event": "Early Exchange Systems",
          "context": "Emergence of organized exchange among agricultural and urban settlements."
        },
        {
          "year": 1776,
          "event": "Classical Market Theory",
          "context": "Formal analysis of markets as coordination mechanisms in political economy."
        },
        {
          "year": 1870,
          "event": "Marginalist Revolution",
          "context": "Markets modeled through supply, demand, and marginal utility."
        },
        {
          "year": 1950,
          "event": "Modern Market Design",
          "context": "Formalization of market mechanisms using game theory and mechanism design."
        },
        {
          "year": 2000,
          "event": "Digital Platform Markets",
          "context": "Expansion of algorithmically mediated and globally connected markets."
        }
      ]
    },
    "specific": {
      "onticLayer": "Synontic",
      "onticCategory": "Institutional",
      "realityDescription": "An emergent institutional structure governing exchange relationships among economic agents.",
      "latentStructures": [
        "Property Rights Systems",
        "Contract Enforcement Mechanisms",
        "Information Structures",
        "Competitive Dynamics",
        "Price Formation Mechanisms",
        "Trust Networks",
        "Regulatory Frameworks"
      ]
    },
    "relationships": [
      {
        "relationshipFamily": "COMPOSITIONAL",
        "relationshipType": "PART_OF",
        "targetNodeId": "economic.system",
        "description": "Markets are constituent institutional structures of economic systems."
      },
      {
        "relationshipFamily": "STRUCTURAL",
        "relationshipType": "DEPENDS_ON",
        "targetNodeId": "property.rights",
        "description": "Markets depend upon stable property rights definitions."
      },
      {
        "relationshipFamily": "STRUCTURAL",
        "relationshipType": "DEPENDS_ON",
        "targetNodeId": "contract",
        "description": "Market exchange relies on contractual arrangements."
      },
      {
        "relationshipFamily": "STRUCTURAL",
        "relationshipType": "DEPENDS_ON",
        "targetNodeId": "price",
        "description": "Prices function as key coordination signals within markets."
      },
      {
        "relationshipFamily": "STRUCTURAL",
        "relationshipType": "DEPENDS_ON",
        "targetNodeId": "economic.agent",
        "description": "Markets emerge from interactions among economic agents."
      },
      {
        "relationshipFamily": "MARKET_RELATION",
        "relationshipType": "ENABLES",
        "targetNodeId": "exchange",
        "description": "Markets provide the institutional environment for exchange."
      },
      {
        "relationshipFamily": "MARKET_RELATION",
        "relationshipType": "ENABLES",
        "targetNodeId": "competition",
        "description": "Markets enable competitive interaction among participants."
      }
    ],
    "metadata": {
      "tags": [
        "market",
        "institution",
        "exchange",
        "price-system",
        "economic-coordination",
        "competition",
        "allocation"
      ],
      "confidenceScore": 0.97,
      "sourceReference": "Sociognosis Economic Ontology",
      "createdAt": "2026-06-10T00:00:00Z",
      "auditTrail": [
        {
          "reviewDate": "2026-06-10",
          "reviewNote": "Initial ontology specification."
        }
      ]
    },
    "references": [
      {
        "title": "Market Institution",
        "description": "Institutional arrangement enabling economic exchange and coordination."
      },
      {
        "title": "Price System",
        "description": "Mechanism through which markets coordinate decentralized decisions."
      }
    ]
  }
]

## See some examples of a visualization of the data - follow the style - but not the structure - you can copy thing thougth

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Space Explorer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap"
        rel="stylesheet">

    <style>

:root {
    /* Increased baseline brightness for surfaces */
    --bg-void: #0a0c14;
    --bg-surface: #12151f;
    --bg-card: #1a1e2a;
    --bg-elevated: #242938;
    
    /* Significantly brighter text colors for contrast */
    --text-primary: #f4f7fc;
    --text-secondary: #b0b8c8;
    --text-muted: #7a8599;
    
    /* More vibrant accents for luminosity */
    --accent-gold: #e0b860;
    --accent-cyan: #60f0e0;
    --accent-rose: #f07080;
    
    /* Higher visibility borders */
    --border-subtle: rgba(255, 255, 255, 0.12);
    --border-medium: rgba(255, 255, 255, 0.2);
    --glow-cyan: 0 0 25px rgba(96, 240, 224, 0.25);
    
    --font-display: 'Cormorant Garamond', serif;
    --font-body: 'Inter', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    --radius-sm: 5px;
    --radius-md: 8px;
    --radius-lg: 12px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background: var(--bg-void);
    color: var(--text-primary);
    font-family: var(--font-body);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
    letter-spacing: 0.015em;
    display: grid;
    grid-template-columns: 300px 1fr;
    grid-template-rows: 1fr;
    height: 100vh;
    overflow: hidden;
    transition: grid-template-columns .5s cubic-bezier(.22, 1, .36, 1);
    font-feature-settings: 'liga' 1, 'kern' 1;
}

body.sidebar-collapsed {
    grid-template-columns: 0 1fr;
}

main.canvas-area {
    position: relative;
    overflow: hidden;
    /* Lighter base grid pattern for visibility */
    background:
        radial-gradient(circle at 50% 1px, rgba(255, 255, 255, 0.05) 0.5px, transparent 0.5px),
        radial-gradient(ellipse at 50% 40%, #141622 0%, var(--bg-void) 75%),
        radial-gradient(ellipse at 25% 65%, rgba(96, 240, 224, 0.04) 0%, transparent 55%),
        radial-gradient(ellipse at 75% 25%, rgba(224, 184, 96, 0.03) 0%, transparent 55%);
    background-size: 4px 4px, 100% 100%, 100% 100%, 100% 100%;
}

main.canvas-area::after {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: radial-gradient(ellipse at 50% 50%, transparent 35%, rgba(10, 12, 20, 0.6) 100%);
    z-index: 1;
}

canvas#graph-canvas {
    width: 100%;
    height: 100%;
    cursor: grab;
    display: block;
}

canvas#graph-canvas:active { cursor: grabbing; }
canvas#graph-canvas.locked { cursor: default; }
canvas#graph-canvas.locked:active { cursor: default; }

.sidebar-toggle {
    position: absolute;
    top: 20px;
    left: 20px;
    z-index: 20;
    background: rgba(16, 18, 28, 0.9);
    backdrop-filter: blur(20px) saturate(1.2);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: var(--text-secondary);
    width: 38px;
    height: 38px;
    border-radius: var(--radius-md);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    transition: all .3s ease;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
}

.sidebar-toggle:hover {
    color: var(--accent-cyan);
    border-color: rgba(96, 240, 224, 0.4);
    box-shadow: var(--glow-cyan), 0 4px 24px rgba(0, 0, 0, 0.5);
}

body.sidebar-collapsed .sidebar-toggle {
    animation: togglePulse 2.5s ease-in-out infinite;
}

@keyframes togglePulse {
    0%, 100% { border-color: rgba(255, 255, 255, 0.15); }
    50% { border-color: rgba(96, 240, 224, 0.3); }
}

.projection-pill {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 15;
    background: rgba(16, 18, 28, 0.92);
    backdrop-filter: blur(24px) saturate(1.2);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: var(--radius-lg);
    padding: 3px;
    display: flex;
    gap: 2px;
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.55);
    --pill-left: 0px;
    --pill-width: 0px;
}

.projection-pill::before {
    content: '';
    position: absolute;
    height: calc(100% - 6px);
    top: 3px;
    left: var(--pill-left);
    width: var(--pill-width);
    background: rgba(96, 240, 224, 0.1);
    border: 1px solid rgba(96, 240, 224, 0.25);
    border-radius: 7px;
    transition: left .35s cubic-bezier(0.22, 1, 0.36, 1), width .35s cubic-bezier(0.22, 1, 0.36, 1);
    pointer-events: none;
    z-index: -1;
}

.proj-chip {
    font-family: var(--font-body);
    font-size: .67rem;
    font-weight: 500;
    letter-spacing: .025em;
    padding: 7px 15px;
    background: transparent;
    border: 1px solid transparent;
    color: var(--text-secondary);
    cursor: pointer;
    transition: color .25s ease, background .25s ease;
    border-radius: var(--radius-md);
    white-space: nowrap;
    position: relative;
    z-index: 1;
}

.proj-chip:hover { color: var(--text-primary); }
.proj-chip.active { color: var(--accent-cyan); }

.quick-actions {
    position: absolute;
    bottom: 44px;
    right: 20px;
    z-index: 15;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.qa-btn {
    width: 36px;
    height: 36px;
    border-radius: var(--radius-md);
    background: rgba(16, 18, 28, 0.92);
    backdrop-filter: blur(20px) saturate(1.2);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: var(--text-secondary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    transition: all .3s cubic-bezier(.22, 1, .36, 1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
}

.qa-btn:hover {
    color: var(--accent-cyan);
    border-color: rgba(96, 240, 224, 0.4);
    background: rgba(96, 240, 224, 0.08);
    transform: scale(1.08);
    box-shadow: var(--glow-cyan), 0 4px 20px rgba(0, 0, 0, 0.45);
}

.minimap-wrap {
    position: absolute;
    bottom: 44px;
    left: 20px;
    z-index: 15;
    width: 180px;
    height: 125px;
    background: rgba(16, 18, 28, 0.92);
    backdrop-filter: blur(20px) saturate(1.2);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 0 8px 36px rgba(0, 0, 0, 0.55);
    cursor: pointer;
    transition: all .3s;
}

.minimap-wrap:hover {
    border-color: rgba(96, 240, 224, 0.3);
    box-shadow: 0 8px 36px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(96, 240, 224, 0.15);
}

.minimap-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: var(--radius-lg);
    box-shadow: inset 0 0 24px rgba(6, 7, 16, 0.7);
    pointer-events: none;
    z-index: 2;
}

.empty-state {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 5;
    pointer-events: none;
    opacity: 0;
    transition: opacity .4s;
}

.empty-state.visible { opacity: 1; }

.empty-state-icon {
    font-family: var(--font-display);
    font-size: 3rem;
    color: var(--text-secondary);
    opacity: .25;
    margin-bottom: 12px;
}

.empty-state-text {
    font-size: .85rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

.empty-state-hint {
    font-family: var(--font-mono);
    font-size: .6rem;
    color: var(--text-muted);
    margin-top: 8px;
}

footer.status-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 28px;
    background: linear-gradient(90deg, rgba(10, 12, 20, 0) 0%, rgba(10, 12, 20, 0.9) 12%, rgba(10, 12, 20, 0.98) 50%, rgba(10, 12, 20, 0.9) 88%, rgba(10, 12, 20, 0) 100%);
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 0;
    padding: 0 20px;
    z-index: 4;
    font-family: var(--font-mono);
    font-size: .6rem;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
    letter-spacing: .03em;
}

footer.status-bar span { padding: 0 12px; position: relative; }
footer.status-bar span + span::before {
    content: '';
    position: absolute;
    left: 0;
    top: 30%;
    height: 40%;
    width: 1px;
    background: rgba(255, 255, 255, 0.12);
}
footer.status-bar span span { color: var(--text-primary); font-weight: 500; padding: 0; }

aside.toolbox {
    background:
        radial-gradient(ellipse 60% 30% at 50% 0%, rgba(224, 184, 96, 0.06) 0%, transparent 100%),
        linear-gradient(180deg, #14120e 0%, #100e0c 100%);
    border-right: 1px solid rgba(224, 184, 96, 0.12);
    padding: 32px 24px 28px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    z-index: 10;
    position: relative;
    transition: all .5s cubic-bezier(.22, 1, .36, 1);
}

body.sidebar-collapsed aside.toolbox {
    opacity: 0;
    pointer-events: none;
    transform: translateX(-100%);
    overflow: hidden;
}

aside.toolbox::-webkit-scrollbar { width: 4px; }
aside.toolbox::-webkit-scrollbar-track { background: transparent; }
aside.toolbox::-webkit-scrollbar-thumb { background: rgba(224, 184, 96, 0.15); border-radius: 3px; }

aside.toolbox::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 8%, rgba(224, 184, 96, 0.5) 50%, transparent 92%);
    z-index: 2;
}

.sb-header { padding-bottom: 26px; position: relative; z-index: 1; }

.sb-eyebrow {
    font-family: var(--font-display);
    font-size: .72rem;
    font-weight: 400;
    font-style: italic;
    color: rgba(224, 184, 96, 0.7);
    letter-spacing: .06em;
    margin-bottom: 12px;
    display: block;
}

.sb-title {
    font-family: var(--font-display);
    font-size: 2.1rem;
    font-style: italic;
    color: var(--text-primary);
    margin-bottom: 8px;
    font-weight: 300;
    line-height: 1.08;
    letter-spacing: .005em;
}

.sb-title::after {
    content: '';
    display: block;
    width: 22px;
    height: 1px;
    margin-top: 14px;
    border-radius: 1px;
    background: var(--accent-gold);
    opacity: .7;
}

.sb-subtitle {
    font-family: var(--font-display);
    font-size: .8rem;
    color: rgba(255, 255, 255, 0.6);
    line-height: 1.55;
    font-weight: 300;
    font-style: italic;
    letter-spacing: .003em;
    margin-top: 2px;
}

.sb-search { position: relative; z-index: 1; padding-bottom: 2px; }
.search-wrap { position: relative; }

.search-box {
    width: 100%;
    background: rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(224, 184, 96, 0.15);
    color: var(--text-primary);
    font-family: var(--font-body);
    font-size: .76rem;
    padding: 10px 32px 10px 36px;
    outline: 0;
    transition: border-color .3s ease, box-shadow .3s ease;
    border-radius: 7px;
    letter-spacing: .005em;
}

.search-box::placeholder {
    color: rgba(255, 255, 255, 0.4);
    font-weight: 300;
    font-style: italic;
}

.search-box:focus {
    border-color: rgba(224, 184, 96, 0.5);
    box-shadow: 0 0 0 3px rgba(224, 184, 96, 0.1);
}

.search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: rgba(255, 255, 255, 0.35);
    pointer-events: none;
}

.search-clear {
    position: absolute;
    right: 6px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    font-size: 15px;
    width: 22px;
    height: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-sm);
    transition: all .2s;
    opacity: 0;
    pointer-events: none;
}

.search-clear.visible { opacity: .6; pointer-events: auto; }
.search-clear:hover { opacity: 1; color: var(--accent-gold); }

.search-selected {
    display: none;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
    padding: 8px 12px;
    background: rgba(224, 184, 96, 0.08);
    border: 1px solid rgba(224, 184, 96, 0.2);
    border-radius: 7px;
    animation: ssIn .25s cubic-bezier(.22, 1, .36, 1);
}

.search-selected.visible { display: flex; }

@keyframes ssIn {
    from { opacity: 0; transform: translateY(-3px); }
    to { opacity: 1; transform: translateY(0); }
}

.search-selected-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

.search-selected-name {
    font-family: var(--font-display);
    font-size: .76rem;
    color: var(--text-primary);
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-weight: 400;
    letter-spacing: .003em;
    font-style: italic;
}

.search-selected-clear {
    background: none;
    border: none;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 12px;
    line-height: 1;
    padding: 0 2px;
    transition: color .2s;
    flex-shrink: 0;
    opacity: .5;
}

.search-selected-clear:hover { opacity: 1; color: var(--accent-gold); }

.sb-gold-line {
    height: 1px;
    margin: 8px 0 0;
    background: linear-gradient(90deg, transparent, rgba(224, 184, 96, 0.25), transparent);
    position: relative;
    z-index: 1;
}

.sb-controls { padding-top: 20px; position: relative; z-index: 1; flex: 1; }

.sb-controls-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
}

.sb-controls-head .label {
    font-family: var(--font-display);
    font-size: .7rem;
    font-weight: 400;
    font-style: italic;
    color: rgba(224, 184, 96, 0.6);
    letter-spacing: .04em;
    display: block;
    margin-bottom: 0;
}

.sb-reset {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-family: var(--font-display);
    font-size: .64rem;
    font-style: italic;
    color: rgba(255, 255, 255, 0.5);
    background: none;
    border: none;
    cursor: pointer;
    transition: all .3s ease;
    letter-spacing: .02em;
    opacity: .9;
}

.sb-reset svg { width: 10px; height: 10px; opacity: .7; transition: opacity .3s; }
.sb-reset:hover { opacity: 1; color: rgba(224, 184, 96, 0.9); }
.sb-reset:hover svg { opacity: 1; }
.sb-reset:active { transform: scale(.96); }

.sb-group { position: relative; }
.sb-group + .sb-group {
    padding-top: 16px;
    margin-top: 16px;
    border-top: 1px solid rgba(224, 184, 96, 0.1);
}

.sb-group-label {
    font-family: var(--font-display);
    font-size: .7rem;
    font-weight: 400;
    font-style: italic;
    color: rgba(224, 184, 96, 0.6);
    letter-spacing: .04em;
    margin-bottom: 9px;
    display: block;
}

.sb-layer-header {
    font-family: var(--font-mono);
    font-size: .5rem;
    font-weight: 500;
    letter-spacing: .08em;
    text-transform: uppercase;
    padding: 7px 7px 3px;
    color: rgba(255, 255, 255, 0.25);
    display: flex;
    align-items: center;
    gap: 6px;
}

.sb-layer-header-dot { width: 4px; height: 4px; border-radius: 50%; flex-shrink: 0; }

.sb-layer-header-count {
    font-family: var(--font-mono);
    font-size: .4rem;
    color: rgba(255, 255, 255, 0.2);
    margin-left: auto;
    font-variant-numeric: tabular-nums;
}

.time-section {
    background: linear-gradient(180deg, rgba(224, 184, 96, 0.04) 0%, transparent 100%);
    border: 1px solid rgba(224, 184, 96, 0.12);
    border-radius: 8px;
    padding: 13px 15px;
    position: relative;
    overflow: hidden;
}

.time-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(224, 184, 96, 0.25), transparent);
}

.time-range {
    display: flex;
    justify-content: space-between;
    font-family: var(--font-mono);
    font-size: .7rem;
    color: rgba(224, 184, 96, 0.9);
    font-weight: 400;
    margin-bottom: 8px;
    font-variant-numeric: tabular-nums;
    letter-spacing: .01em;
}

.time-slider-wrap { position: relative; height: 16px; margin-bottom: 6px; }

.time-track {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 1px;
    background: rgba(255, 255, 255, 0.12);
    transform: translateY(-50%);
    border-radius: 1px;
}

.time-fill {
    position: absolute;
    top: 50%;
    height: 1px;
    background: var(--accent-gold);
    transform: translateY(-50%);
    border-radius: 1px;
    pointer-events: none;
    transition: left .05s, width .05s;
    opacity: .6;
}

.time-fill.active { opacity: 1; box-shadow: 0 0 12px rgba(224, 184, 96, 0.25); }

.time-slider-wrap input[type=range] {
    -webkit-appearance: none;
    appearance: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: transparent;
    margin: 0;
    outline: none;
    pointer-events: none;
    z-index: 2;
}

.time-slider-wrap input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    pointer-events: all;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: var(--accent-gold);
    border: none;
    cursor: ew-resize;
    box-shadow: 0 0 10px rgba(224, 184, 96, 0.5);
    transition: box-shadow .2s, transform .15s;
}

.time-slider-wrap input[type=range]::-webkit-slider-thumb:hover {
    box-shadow: 0 0 18px rgba(224, 184, 96, 0.7);
    transform: scale(1.15);
}

.time-slider-wrap input[type=range]::-moz-range-thumb {
    pointer-events: all;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: var(--accent-gold);
    border: none;
    cursor: ew-resize;
    box-shadow: 0 0 10px rgba(224, 184, 96, 0.5);
}

.time-slider-wrap input[type=range]::-moz-range-track { background: transparent; border: none; }

.time-stats {
    display: flex;
    align-items: center;
    gap: 5px;
    font-family: var(--font-mono);
    font-size: .48rem;
    color: var(--text-secondary);
    font-variant-numeric: tabular-nums;
    letter-spacing: .01em;
}

.time-stats .ts-count { color: var(--accent-gold); font-weight: 500; font-size: .62rem; }
.time-stats .ts-dot { width: 2px; height: 2px; border-radius: 50%; background: rgba(224, 184, 96, 0.6); }

.toggle-group { display: flex; flex-direction: column; gap: 1px; }

.toggle-item {
    display: flex;
    align-items: center;
    gap: 9px;
    cursor: pointer;
    font-size: .68rem;
    color: var(--text-secondary);
    transition: all .2s ease;
    padding: 5px 8px;
    border-radius: 5px;
    border: 1px solid transparent;
    letter-spacing: .004em;
}

.toggle-item:hover {
    color: var(--text-primary);
    background: rgba(224, 184, 96, 0.05);
}

.toggle-item input { display: none; }

.checkmark {
    width: 14px;
    height: 14px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all .2s;
    flex-shrink: 0;
    border-radius: 3px;
}

.toggle-item input:checked ~ .checkmark {
    border-color: rgba(224, 184, 96, 0.7);
    background: rgba(224, 184, 96, 0.15);
}

.toggle-item input:checked ~ .checkmark::after {
    content: '';
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--accent-gold);
    opacity: 1;
}

.toggle-item.disabled { opacity: .2; pointer-events: none; }

.cat-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }

.node-count {
    font-family: var(--font-mono);
    font-size: .44rem;
    color: var(--text-muted);
    margin-left: auto;
    font-variant-numeric: tabular-nums;
}

.toggle-item { animation: toggleIn .3s ease-out backwards; }
.toggle-item:nth-child(1) { animation-delay: .02s; }
.toggle-item:nth-child(2) { animation-delay: .04s; }
.toggle-item:nth-child(3) { animation-delay: .06s; }
.toggle-item:nth-child(4) { animation-delay: .08s; }
.toggle-item:nth-child(5) { animation-delay: .10s; }
.toggle-item:nth-child(6) { animation-delay: .12s; }
.toggle-item:nth-child(7) { animation-delay: .14s; }
.toggle-item:nth-child(8) { animation-delay: .16s; }
.toggle-item:nth-child(9) { animation-delay: .18s; }
.toggle-item:nth-child(10) { animation-delay: .20s; }

@keyframes toggleIn {
    from { opacity: 0; transform: translateX(-3px); }
    to { opacity: 1; transform: translateX(0); }
}

.chip-grid { display: flex; flex-wrap: wrap; gap: 5px; }

.chip {
    font-family: var(--font-body);
    font-size: .6rem;
    font-weight: 400;
    padding: 5px 10px;
    background: rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.1);
    cursor: pointer;
    transition: all .2s ease, color .15s ease;
    color: var(--text-secondary);
    border-radius: 5px;
    border-left-width: 2.5px;
    white-space: nowrap;
    letter-spacing: .004em;
}

.chip:hover {
    color: var(--text-primary);
    background: rgba(224, 184, 96, 0.08);
}

.chip.active {
    color: var(--text-primary);
    background: rgba(224, 184, 96, 0.12);
    border-color: rgba(224, 184, 96, 0.3);
}

.search-dropdown {
    position: fixed;
    z-index: 500;
    background: rgba(12, 11, 9, 0.98);
    backdrop-filter: blur(36px) saturate(1.15);
    border: 1px solid rgba(224, 184, 96, 0.15);
    border-radius: 10px;
    box-shadow: 0 24px 72px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(224, 184, 96, 0.05) inset;
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: max-height .35s cubic-bezier(.22, 1, .36, 1), opacity .2s ease;
    pointer-events: none;
    width: 360px;
}

.search-dropdown.open { max-height: 440px; opacity: 1; pointer-events: auto; }

.search-dropdown-header {
    padding: 10px 14px 8px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1px solid rgba(224, 184, 96, 0.1);
}

.search-dropdown-label {
    font-family: var(--font-display);
    font-size: .58rem;
    font-style: italic;
    color: rgba(224, 184, 96, 0.7);
    letter-spacing: .04em;
}

.search-dropdown-count {
    font-family: var(--font-mono);
    font-size: .42rem;
    color: var(--text-muted);
    letter-spacing: .06em;
}

.search-dropdown-inner {
    max-height: 380px;
    overflow-y: auto;
    padding: 4px 5px;
    scrollbar-width: thin;
    scrollbar-color: rgba(224, 184, 96, 0.1) transparent;
}

.search-dropdown-inner::-webkit-scrollbar { width: 3px; }
.search-dropdown-inner::-webkit-scrollbar-track { background: transparent; }
.search-dropdown-inner::-webkit-scrollbar-thumb { background: rgba(224, 184, 96, 0.1); border-radius: 3px; }

.search-result {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 9px 9px;
    cursor: pointer;
    transition: all .15s ease;
    border-radius: 6px;
    border: 1px solid transparent;
}

.search-result + .search-result { margin-top: 1px; }

.search-result:hover,
.search-result.kb-focus {
    background: rgba(224, 184, 96, 0.05);
    border-color: rgba(224, 184, 96, 0.15);
}

.search-result.kb-focus {
    background: rgba(224, 184, 96, 0.08);
    border-color: rgba(224, 184, 96, 0.25);
}

.search-result.active {
    background: rgba(224, 184, 96, 0.12);
    border-color: rgba(224, 184, 96, 0.35);
}

.search-result.active .sr-name { color: var(--accent-gold); }

.sr-cat-line {
    width: 1px;
    align-self: stretch;
    flex-shrink: 0;
    border-radius: 1px;
    margin: 2px 0;
    opacity: .4;
    transition: opacity .2s;
}

.search-result:hover .sr-cat-line,
.search-result.kb-focus .sr-cat-line,
.search-result.active .sr-cat-line { opacity: .8; }

.sr-body { flex: 1; min-width: 0; padding-top: 1px; }

.sr-top { display: flex; align-items: baseline; gap: 7px; margin-bottom: 2px; }

.sr-name {
    font-family: var(--font-display);
    font-size: .8rem;
    color: var(--text-primary);
    font-weight: 400;
    font-style: italic;
    letter-spacing: .003em;
    line-height: 1.2;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    transition: color .15s;
}

.sr-name mark {
    background: rgba(224, 184, 96, 0.2);
    color: var(--accent-gold);
    border-radius: 1px;
    padding: 0 1px;
    font-style: italic;
}

.sr-cat-label {
    font-family: var(--font-mono);
    font-size: .4rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    flex-shrink: 0;
    opacity: .6;
    font-weight: 500;
    transition: opacity .2s;
}

.search-result:hover .sr-cat-label,
.search-result.kb-focus .sr-cat-label { opacity: .9; }

.sr-desc {
    font-size: .56rem;
    color: var(--text-secondary);
    line-height: 1.45;
    font-weight: 300;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.sr-foot {
    display: flex;
    gap: 10px;
    margin-top: 3px;
    font-family: var(--font-mono);
    font-size: .38rem;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
    letter-spacing: .03em;
}

.sr-layer-label {
    font-family: var(--font-mono);
    font-size: .38rem;
    color: var(--text-muted);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 0 4px;
    border-radius: 2px;
    line-height: 1.6;
}

.search-empty-hint {
    padding: 28px 20px;
    text-align: center;
    color: var(--text-secondary);
    font-size: .7rem;
    opacity: .7;
    font-weight: 300;
    letter-spacing: .01em;
    font-style: italic;
    font-family: var(--font-display);
}

#tooltip {
    position: absolute;
    display: none;
    background: rgba(14, 16, 26, 0.98);
    backdrop-filter: blur(20px) saturate(1.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-left: 2px solid transparent;
    border-image: linear-gradient(180deg, var(--accent-cyan), transparent) 1;
    padding: 14px 16px;
    width: 270px;
    pointer-events: none;
    z-index: 100;
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.7);
    border-radius: var(--radius-md) 0 var(--radius-md) var(--radius-md);
    animation: ttIn .15s ease-out;
}

@keyframes ttIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
}

.tt-title {
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-style: italic;
    margin-bottom: 3px;
    line-height: 1.2;
    font-weight: 400;
    letter-spacing: .005em;
    color: var(--text-primary);
}

.tt-cat {
    font-family: var(--font-mono);
    font-size: .54rem;
    text-transform: uppercase;
    letter-spacing: .12em;
    margin-bottom: 2px;
    font-weight: 500;
}

.tt-layer {
    font-family: var(--font-mono);
    font-size: .48rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    margin-bottom: 6px;
    font-weight: 500;
    opacity: .8;
}

.tt-desc {
    font-size: .72rem;
    color: var(--text-secondary);
    line-height: 1.55;
    font-weight: 300;
}

.tt-year {
    font-family: var(--font-mono);
    font-size: .54rem;
    color: var(--accent-cyan);
    margin-top: 5px;
    opacity: .8;
    font-variant-numeric: tabular-nums;
}

.tt-meta {
    display: flex;
    gap: 10px;
    margin-top: 6px;
    font-family: var(--font-mono);
    font-size: .52rem;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
}

.tt-meta span { display: flex; align-items: center; gap: 3px; }

#inspect-panel {
    position: absolute;
    top: 0;
    right: 0;
    width: 380px;
    height: 100%;
    background: var(--bg-surface);
    border-left: 1px solid var(--border-medium);
    z-index: 150;
    transform: translateX(100%);
    transition: transform .45s cubic-bezier(.22, 1, .36, 1);
    overflow-y: auto;
    box-shadow: -12px 0 48px rgba(0, 0, 0, 0.6), -1px 0 0 0 rgba(255, 255, 255, 0.05);
}

#inspect-panel.open { transform: translateX(0); }

#inspect-panel::-webkit-scrollbar { width: 3px; }
#inspect-panel::-webkit-scrollbar-track { background: transparent; }
#inspect-panel::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 3px; }

.ip-accent-bar { height: 2px; border-radius: 0 0 1px 1px; }

.ip-header {
    padding: 32px 28px 24px;
    position: relative;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.04) 0%, transparent 100%);
}

.ip-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--border-medium);
    color: var(--text-secondary);
    width: 28px;
    height: 28px;
    cursor: pointer;
    font-family: var(--font-mono);
    font-size: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-sm);
    transition: all .2s;
}

.ip-close:hover {
    color: var(--text-primary);
    border-color: var(--text-muted);
    background: rgba(255, 255, 255, 0.12);
}

.ip-category-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-mono);
    font-size: .58rem;
    text-transform: uppercase;
    letter-spacing: .12em;
    padding: 3px 10px;
    border-radius: 3px;
    margin-bottom: 6px;
    border: 1px solid;
    font-weight: 500;
}

.ip-layer-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-family: var(--font-mono);
    font-size: .5rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    padding: 2px 8px;
    border-radius: 3px;
    margin-bottom: 12px;
    border: 1px solid;
    font-weight: 500;
}

.ip-category-dot, .ip-layer-dot { width: 5px; height: 5px; border-radius: 50%; }

.ip-node-name {
    font-family: var(--font-display);
    font-size: 1.75rem;
    font-style: italic;
    line-height: 1.15;
    margin-bottom: 10px;
    color: var(--text-primary);
    font-weight: 300;
    letter-spacing: .008em;
}

.ip-node-desc {
    font-size: .78rem;
    color: var(--text-secondary);
    line-height: 1.6;
    font-weight: 300;
    letter-spacing: .005em;
}

.ip-stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 1px;
    background: var(--border-medium);
    border-top: 1px solid var(--border-medium);
    border-bottom: 1px solid var(--border-medium);
}

.ip-stat { background: var(--bg-surface); padding: 14px 12px; text-align: center; }
.ip-stat-value {
    font-family: var(--font-mono);
    font-size: 1rem;
    font-weight: 500;
    margin-bottom: 2px;
    font-variant-numeric: tabular-nums;
    letter-spacing: .02em;
}
.ip-stat-label {
    font-family: var(--font-mono);
    font-size: .42rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .06em;
}

.ip-divider { display: flex; align-items: center; gap: 12px; padding: 0 28px; height: 1px; background: var(--border-medium); }
.ip-diamond { width: 5px; height: 5px; background: var(--accent-cyan); opacity: .5; transform: rotate(45deg); flex-shrink: 0; }

.ip-section {
    padding: 18px 28px;
    border-bottom: 1px solid var(--border-medium);
    animation: secIn .3s ease-out backwards;
}

@keyframes secIn {
    from { opacity: 0; transform: translateX(10px); }
    to { opacity: 1; transform: translateX(0); }
}

.ip-section-title {
    font-family: var(--font-body);
    font-size: .6rem;
    font-weight: 600;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: .1em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.ip-section-title::before {
    content: '';
    width: 2px;
    height: 10px;
    border-radius: 1px;
    background: var(--accent-cyan);
    opacity: .6;
}

.ip-tags { display: flex; flex-wrap: wrap; gap: 5px; }

.ip-tag {
    font-family: var(--font-mono);
    font-size: .56rem;
    padding: 3px 8px;
    background: rgba(0, 0, 0, 0.35);
    border: 1px solid var(--border-subtle);
    color: var(--text-secondary);
    border-radius: 3px;
    transition: all .2s;
    letter-spacing: .01em;
}

.ip-tag:hover { border-color: rgba(96, 240, 224, 0.3); color: var(--text-primary); }

.ip-edge-list { list-style: none; }

.ip-edge-item {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    transition: background .2s;
}

.ip-edge-item:last-child { border-bottom: none; }
.ip-edge-item:hover { background: rgba(255, 255, 255, 0.03); border-radius: var(--radius-sm); }

.ip-edge-connector { width: 20px; display: flex; flex-direction: column; align-items: center; flex-shrink: 0; padding-top: 2px; }
.ip-edge-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }

.ip-edge-content { flex: 1; min-width: 0; }

.ip-edge-type {
    font-family: var(--font-mono);
    font-size: .58rem;
    padding: 1px 6px;
    border-radius: 2px;
    display: inline-block;
    margin-bottom: 2px;
    letter-spacing: .01em;
}

.ip-edge-target {
    font-size: .78rem;
    color: var(--text-primary);
    display: block;
    font-weight: 400;
    letter-spacing: .005em;
}

.ip-edge-desc {
    font-family: var(--font-mono);
    font-size: .54rem;
    color: var(--text-muted);
    margin-top: 1px;
    display: block;
    line-height: 1.5;
}

.ip-prop-list { display: flex; flex-direction: column; gap: 6px; }

.ip-prop-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 8px;
    padding: 4px 0;
}

.ip-prop-key {
    font-family: var(--font-mono);
    font-size: .58rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .04em;
    flex-shrink: 0;
}

.ip-prop-val {
    font-family: var(--font-mono);
    font-size: .68rem;
    color: var(--text-secondary);
    text-align: right;
    word-break: break-word;
    letter-spacing: .005em;
}

.ip-audit-item {
    position: relative;
    padding: 6px 0 6px 16px;
    border-left: 2px solid var(--border-medium);
    margin-left: 4px;
}

.ip-audit-date {
    font-family: var(--font-mono);
    font-size: .52rem;
    color: var(--accent-cyan);
    opacity: .8;
    margin-bottom: 1px;
    font-variant-numeric: tabular-nums;
}

.ip-audit-note { font-size: .68rem; color: var(--text-secondary); line-height: 1.5; font-weight: 300; }

.ip-chron-item {
    position: relative;
    padding: 6px 0 6px 16px;
    border-left: 2px solid rgba(224, 184, 96, 0.3);
    margin-left: 4px;
}

.ip-chron-item:last-child { border-left-color: var(--accent-gold); }

.ip-chron-year {
    font-family: var(--font-mono);
    font-size: .52rem;
    color: var(--accent-gold);
    opacity: .9;
    margin-bottom: 1px;
    font-variant-numeric: tabular-nums;
}

.ip-chron-event { font-size: .68rem; color: var(--text-secondary); line-height: 1.5; font-weight: 300; letter-spacing: .003em; }
.ip-chron-ctx { font-family: var(--font-mono); font-size: .5rem; color: var(--text-muted); margin-top: 1px; line-height: 1.45; }

.ip-long-desc-block {
    padding: 18px 28px;
    border-bottom: 1px solid var(--border-medium);
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.03) 0%, transparent 100%);
    animation: secIn .3s ease-out backwards;
}

.ip-long-desc-text {
    font-size: .74rem;
    color: var(--text-secondary);
    line-height: 1.75;
    font-weight: 300;
    letter-spacing: .005em;
    white-space: pre-line;
}

.ip-long-desc-toggle {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-family: var(--font-display);
    font-size: .64rem;
    font-weight: 400;
    font-style: italic;
    color: rgba(224, 184, 96, 0.9);
    cursor: pointer;
    background: none;
    border: none;
    padding: 8px 0 0;
    margin-top: 6px;
    letter-spacing: .02em;
    transition: color .2s, opacity .2s;
    opacity: .9;
}

.ip-long-desc-toggle:hover { opacity: 1; color: var(--accent-gold); }
.ip-long-desc-toggle svg { width: 10px; height: 10px; transition: transform .3s cubic-bezier(.22, 1, .36, 1); }
.ip-long-desc-toggle.expanded svg { transform: rotate(180deg); }

.ip-long-desc-content {
    overflow: hidden;
    transition: max-height .45s cubic-bezier(.22, 1, .36, 1), opacity .35s ease;
    max-height: 0;
    opacity: 0;
}

.ip-long-desc-content.expanded { max-height: 3000px; opacity: 1; }

.ip-long-desc-preview {
    font-size: .74rem;
    color: var(--text-secondary);
    line-height: 1.65;
    font-weight: 300;
    letter-spacing: .005em;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.ip-enum-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-family: var(--font-mono);
    font-size: .58rem;
    text-transform: uppercase;
    letter-spacing: .08em;
    padding: 2px 8px;
    border-radius: 3px;
    border: 1px solid;
    font-weight: 500;
}

.ip-array-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 2px; }

.ip-array-tag {
    font-family: var(--font-mono);
    font-size: .54rem;
    padding: 2px 7px;
    background: rgba(96, 240, 224, 0.1);
    border: 1px solid rgba(96, 240, 224, 0.2);
    color: var(--text-secondary);
    border-radius: 3px;
    letter-spacing: .01em;
}

.ip-hist-summary {
    font-size: .72rem;
    color: var(--text-secondary);
    line-height: 1.6;
    font-weight: 300;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    letter-spacing: .003em;
}

.ip-meta-row { display: flex; align-items: baseline; gap: 8px; padding: 3px 0; }

.ip-meta-key {
    font-family: var(--font-mono);
    font-size: .52rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .05em;
    flex-shrink: 0;
    min-width: 70px;
}

.ip-meta-val {
    font-family: var(--font-mono);
    font-size: .62rem;
    color: var(--text-secondary);
    word-break: break-word;
    letter-spacing: .003em;
}

.ip-meta-val a { color: var(--accent-cyan); text-decoration: none; opacity: .9; transition: opacity .2s; }
.ip-meta-val a:hover { opacity: 1; }

#chord-tooltip {
    position: absolute;
    display: none;
    background: rgba(14, 16, 26, 0.98);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(224, 184, 96, 0.3);
    padding: 8px 12px;
    pointer-events: none;
    z-index: 50;
    font-family: var(--font-mono);
    font-size: .64rem;
    color: var(--text-primary);
    border-radius: var(--radius-sm);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.6);
    font-variant-numeric: tabular-nums;
}

#loading-overlay {
    position: fixed;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: var(--bg-void);
    z-index: 200;
    transition: opacity .8s cubic-bezier(.22, 1, .36, 1);
}

#loading-overlay.hidden { opacity: 0; pointer-events: none; }

.loader-dots { display: flex; gap: 8px; }

.loader-dots span {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--accent-cyan);
    opacity: .25;
    animation: dotPulse 1.4s ease-in-out infinite;
}

.loader-dots span:nth-child(2) { animation-delay: .16s; }
.loader-dots span:nth-child(3) { animation-delay: .32s; }

@keyframes dotPulse {
    0%, 80%, 100% { opacity: .25; transform: scale(.8); }
    40% { opacity: 1; transform: scale(1.3); }
}

.loader-text {
    font-family: var(--font-mono);
    font-size: .6rem;
    color: var(--text-secondary);
    margin-top: 24px;
    text-transform: uppercase;
    letter-spacing: .25em;
    font-weight: 300;
    transition: opacity .4s;
}

.loader-error {
    color: var(--accent-rose);
    max-width: 400px;
    text-align: center;
    line-height: 1.6;
    font-weight: 300;
    letter-spacing: .005em;
}

/* References list */
.ip-ref-list { display: flex; flex-direction: column; gap: 6px; }

.ip-ref-card {
    display: block;
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.04);
    text-decoration: none;
    color: inherit;
    transition: background 0.2s, border-color 0.2s, transform 0.15s;
    animation: ipFadeSlideIn 0.35s ease both;
}

.ip-ref-card:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-1px);
}

.ip-ref-header { display: flex; align-items: center; gap: 10px; }

.ip-ref-icon {
    flex-shrink: 0;
    width: 30px;
    height: 30px;
    border-radius: 6px;
    background: rgba(96, 240, 224, 0.15);
    color: #60f0e0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.ip-ref-icon svg { width: 14px; height: 14px; }

.ip-ref-titles { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 1px; }

.ip-ref-title {
    font-size: 12.5px;
    font-weight: 500;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.3;
}

.ip-ref-domain {
    font-size: 10.5px;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.ip-ref-arrow {
    flex-shrink: 0;
    width: 14px;
    height: 14px;
    color: var(--text-muted);
    transition: color 0.2s, transform 0.2s;
}

.ip-ref-card:hover .ip-ref-arrow { color: #60f0e0; transform: translate(2px, -2px); }

.ip-ref-desc {
    margin-top: 6px;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 11px;
    line-height: 1.55;
    color: var(--text-secondary);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

@keyframes ipFadeSlideIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (prefers-reduced-motion: reduce) {
    .loader-dots span { animation: none; opacity: .5; }
    * { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; }
}

    </style>


</head>

<body>
    <aside class="toolbox" id="sidebar">
        <div class="sb-header"><span class="sb-eyebrow">Product Space Atlas</span>
            <h2 class="sb-title">Space Explorer</h2>
            <p class="sb-subtitle">Mapping the architecture of production capabilities.</p>
        </div>
        <div class="sb-search">
            <div class="search-wrap"><svg class="search-icon" width="13" height="13" viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8" />
                    <line x1="21" y1="21" x2="16.65" y2="16.65" />
                </svg><input type="text" class="search-box" id="search-input" placeholder="Search nodes..."
                    autocomplete="off"><button class="search-clear" id="search-clear">&times;</button></div>
            <div class="search-selected" id="search-selected"><span class="search-selected-dot"
                    id="search-selected-dot"></span><span class="search-selected-name"
                    id="search-selected-name"></span><button class="search-selected-clear"
                    id="search-selected-clear">&times;</button></div>
        </div>
        <div class="sb-gold-line"></div>
        <div class="sb-controls">
            <div class="sb-controls-head"><span class="label">Controls</span><button class="sb-reset"
                    id="reset-all-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="1 4 1 10 7 10" />
                        <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
                    </svg>reset</button></div>
            <div class="sb-group"><span class="sb-group-label">Temporal Scope</span>
                <div class="time-section">
                    <div class="time-range"><span id="time-min-label">&mdash;</span><span
                            id="time-max-label">&mdash;</span></div>
                    <div class="time-slider-wrap">
                        <div class="time-track"></div>
                        <div class="time-fill" id="time-fill"></div><input type="range" id="time-min" min="0" max="1000"
                            value="0"><input type="range" id="time-max" min="0" max="1000" value="1000">
                    </div>
                    <div class="time-stats"><span class="ts-dot"></span><span class="ts-count"
                            id="time-visible-count">0</span><span>of <span id="time-total-count">0</span> nodes</span>
                    </div>
                </div>
            </div>
            <div class="sb-group" id="layer-group" style="display:none"><span class="sb-group-label">Operational Layers</span>
                <div class="toggle-group" id="layer-toggles"></div>
            </div>
            <div class="sb-group"><span class="sb-group-label">Categories</span>
                <div class="toggle-group" id="category-toggles"></div>
            </div>
            <div class="sb-group"><span class="sb-group-label">Relationship Families</span>
                <div class="chip-grid" id="family-chips"></div>
            </div>
            <div class="sb-group"><span class="sb-group-label">Visual Lenses</span>
                <div class="toggle-group" id="lens-controls"><label class="toggle-item"
                        data-conflict="chord,confidence,radial,umap,spectral,bipartite"><input type="checkbox" id="lens-hulls" checked><span
                            class="checkmark"></span>Category Hulls</label><label class="toggle-item"
                        data-conflict="chord,confidence,umap,spectral,bipartite"><input type="checkbox" id="lens-heatmap"><span
                            class="checkmark"></span>Constraint Heatmap</label><label class="toggle-item"
                        data-conflict="chord,umap,spectral,bipartite"><input type="checkbox" id="lens-centrality"><span
                            class="checkmark"></span>Centrality Sizing</label><label class="toggle-item"
                        data-conflict="chord,umap,spectral,bipartite"><input type="checkbox" id="lens-confidence-color"><span
                            class="checkmark"></span>Confidence Gradient</label><label class="toggle-item"
                        data-conflict="chord,umap,spectral,bipartite"><input type="checkbox" id="lens-flow" checked><span
                            class="checkmark"></span>Luminous Flow</label><label class="toggle-item"
                        data-conflict="chord,umap,spectral,bipartite"><input type="checkbox" id="lens-observability"><span
                            class="checkmark"></span>Confidence Ghosting</label></div>
            </div>
        </div>
    </aside>
    <main class="canvas-area">
        <button class="sidebar-toggle" id="sidebar-toggle-btn">&#9776;</button>
        <div class="projection-pill" id="projection-chips">
            <div class="proj-chip active" data-proj="default">Force</div>
            <div class="proj-chip" data-proj="category">Clusters</div>
            <div class="proj-chip" data-proj="layer">Layers</div>
            <div class="proj-chip" data-proj="confidence">Confidence</div>
            <div class="proj-chip" data-proj="radial">Radial</div>
            <div class="proj-chip" data-proj="chord">Chord</div>
            <div class="proj-chip" data-proj="umap">UMAP Embedding</div>
            <div class="proj-chip" data-proj="spectral">Spectral</div>
            <div class="proj-chip" data-proj="bipartite">Bipartite</div>
        </div>
        <canvas id="graph-canvas"></canvas>
        <div class="quick-actions"><button class="qa-btn" id="qa-fit" title="Fit View (F)">&#8862;</button></div>
        <div class="minimap-wrap" id="minimap-wrap"><canvas id="minimap-canvas"></canvas></div>
        <div class="empty-state" id="empty-state">
            <div class="empty-state-icon">&#9675;</div>
            <div class="empty-state-text">No nodes match current filters</div>
            <div class="empty-state-hint">Adjust temporal scope, layers, categories, or families</div>
        </div>
        <footer class="status-bar"><span>Nodes <span id="hud-v">0</span></span><span>Edges <span
                    id="hud-e">0</span></span><span>View <span id="hud-proj">Force</span></span><span id="hud-proj-info"></span><span id="fps-counter">0
                FPS</span></footer>
        <div id="tooltip">
            <div class="tt-cat" id="tt-cat"></div>
            <div class="tt-layer" id="tt-layer"></div>
            <div class="tt-title" id="tt-title"></div>
            <div class="tt-desc" id="tt-desc"></div>
            <div class="tt-year" id="tt-year"></div>
            <div class="tt-meta" id="tt-meta"></div>
        </div>
        <div id="chord-tooltip"></div>
        <div id="inspect-panel">
            <div class="ip-accent-bar" id="ip-accent-bar"></div>
            <div class="ip-header"><button class="ip-close" id="ip-close-btn">&times;</button>
                <div class="ip-category-badge" id="ip-badge"><span class="ip-category-dot"
                        id="ip-badge-dot"></span><span id="ip-badge-text"></span></div>
                <div class="ip-layer-badge" id="ip-layer-badge"><span class="ip-layer-dot"
                        id="ip-layer-dot"></span><span id="ip-layer-text"></span></div>
                <div class="ip-node-name" id="ip-title"></div>
                <div class="ip-node-desc" id="ip-desc"></div>
            </div>
            <div class="ip-stats-grid" id="ip-stats-grid"></div>
            <div class="ip-divider"><span class="ip-diamond"></span></div>
            <div id="ip-dynamic-sections"></div>
        </div>
    </main>
    <div class="search-dropdown" id="search-dropdown">
        <div class="search-dropdown-header"><span class="search-dropdown-label">Results</span><span
                class="search-dropdown-count" id="search-dropdown-count"></span></div>
        <div class="search-dropdown-inner" id="search-dropdown-inner"></div>
    </div>
    <div id="loading-overlay">
        <div class="loader-dots"><span></span><span></span><span></span></div>
        <div class="loader-text" id="loader-msg">Initializing graph</div>
    </div>
    <script>
        /* ═══════ UTILITIES ═══════ */
        function hexToRGBA(h,a){if(!h||h.startsWith('rgb'))return h;var r=parseInt(h.slice(1,3),16),g=parseInt(h.slice(3,5),16),b=parseInt(h.slice(5,7),16);return'rgba('+r+','+g+','+b+','+a+')'}
        function friendlyLabel(k){return k.replace(/([A-Z])/g,' $1').replace(/_/g,' ').replace(/^./,function(s){return s.toUpperCase()}).replace(/\s+/g,' ').trim()}
        function shortLabel(k){var m={'ProductionProcess':'Process','ProductionSystem':'System','ValueChainStage':'Value Chain','ProductionFunction':'Prod. Function','ProductCategory':'Prod. Category'};return m[k]||friendlyLabel(k)}
        function confidenceColor(s){var r,g,b;if(s<=0.5){var t=s/0.5;r=224;g=Math.round(96+128*t);b=Math.round(112+104*t)}else{var t2=(s-0.5)/0.5;r=Math.round(224-152*t2);g=Math.round(224+8*t2);b=216}return'rgb('+r+','+g+','+b+')'}
        function clamp(v,lo,hi){return Math.max(lo,Math.min(hi,v))}
        function hlMatch(text,q){if(!q)return text;var i=text.toLowerCase().indexOf(q.toLowerCase());if(i===-1)return text;return text.substring(0,i)+'<mark>'+text.substring(i,i+q.length)+'</mark>'+text.substring(i+q.length)}
        function isFiniteNum(v){return typeof v==='number'&&isFinite(v)}
        function escHTML(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}

        function drawRoundRect(c,x,y,w,h,r){r=Math.max(0,Math.min(r,Math.min(w,h)/2));c.beginPath();c.moveTo(x+r,y);c.lineTo(x+w-r,y);c.quadraticCurveTo(x+w,y,x+w,y+r);c.lineTo(x+w,y+h-r);c.quadraticCurveTo(x+w,y+h,x+w-r,y+h);c.lineTo(x+r,y+h);c.quadraticCurveTo(x,y+h,x,y+h-r);c.lineTo(x,y+r);c.quadraticCurveTo(x,y,x+r,y);c.closePath()}

        /* ═══════ SCHEMA-ALIGNED CONSTANTS ═══════ */
        var CP=['#FF9F43','#48e8d8','#7EC8E8','#3CC0A0','#80C090','#5DE8C8','#70E0B8','#E8E8E8','#C0A060','#C03050','#45D4A0','#F070B0','#7BE0A0','#5090D0','#45B7D1','#40C880','#FF6B6B','#C0785A','#D04050','#FFE066','#A0D0A0'];
        var FP=['#48e8d8','#C9A44e','#7BE0A0','#E06070','#FFE066','#8B7BF0','#C0785A','#45B7D1','#90A8C0'];
        var SC=['circle','triangle','square','diamond','hexagon'];

        /* Category → Derived Layer mapping (schema has no layer field) */
        var CLL={
            'Product':'Product Space','ProductCategory':'Product Space',
            'ProductionProcess':'Process Space','ProductionSystem':'Process Space',
            'ValueChainStage':'Process Space','ProductionFunction':'Process Space',
            'Technique':'Capability Space','Capability':'Capability Space','Research':'Capability Space',
            'Resource':'Infrastructure Space','Infrastructure':'Infrastructure Space','Institution':'Infrastructure Space',
            'Specification':'Product Space','Standard':'Governance Space',
            'Strategy':'Strategic Space','Market':'Strategic Space','Problem':'Strategic Space',
            'Evolution':'Evolution Space','Failure':'Evolution Space','Constraint':'Evolution Space'
        };
        var LPC={
            'Strategic Space':'#C9A44e','Capability Space':'#48e8d8','Process Space':'#7BE0A0',
            'Product Space':'#45B7D1','Infrastructure Space':'#E06070','Governance Space':'#90A8C0','Evolution Space':'#8B7BF0'
        };

        /* Relationship family friendly labels */
        var FLM={
            'FUNCTIONAL':'Functional','STRUCTURAL':'Structural',
            'CAPABILITY_DEPENDENCY':'Capability Dep.','VALUE_CHAIN':'Value Chain',
            'MARKET_RELATION':'Market','GOVERNANCE':'Governance',
            'TEMPORAL_EVOLUTION':'Temporal','COMPOSITIONAL':'Compositional','CLASSIFICATION':'Classification'
        };

        /* Default type→family mapping (overridden by data if present) */
        var TFM_DEFAULT={
            'PRODUCES':'VALUE_CHAIN','CONSUMES':'VALUE_CHAIN',
            'ENABLES':'CAPABILITY_DEPENDENCY','REQUIRES':'CAPABILITY_DEPENDENCY','DEPENDS_ON':'CAPABILITY_DEPENDENCY',
            'PART_OF':'COMPOSITIONAL','TRANSFORMS_INTO':'FUNCTIONAL','COMPLEMENTS':'FUNCTIONAL',
            'SPECIALIZES':'CLASSIFICATION','GENERALIZES':'CLASSIFICATION',
            'COMPLIES_WITH':'GOVERNANCE','ORCHESTRATED_BY':'GOVERNANCE',
            'CONSTRAINED_BY':'STRUCTURAL',
            'COMPETES_WITH':'MARKET_RELATION','SUBSTITUTES_FOR':'MARKET_RELATION',
            'EVOLVES_FROM':'TEMPORAL_EVOLUTION','SUPERSEDES':'TEMPORAL_EVOLUTION'
        };

        /* Bipartite grouping by derived layer */
        var BIP_LEFT=['Process Space','Capability Space'];
        var BIP_RIGHT=['Product Space','Infrastructure Space','Governance Space'];

        var CL=[],CLB={},CC={},CS={};
        var LL=[],LLB={},LC={};
        var FL=[],FC={},FLB={},TFM={};
        var PL={default:'Force',category:'Clusters',layer:'Layers',confidence:'Confidence',radial:'Radial',chord:'Chord',umap:'UMAP',spectral:'Spectral',bipartite:'Bipartite'};
        var SP=['confidence','radial','umap','spectral','bipartite'];

        var aCats=new Set(),aFams=new Set(),aLayers=new Set();

        function deriveSchema(data){
            var cs=new Set(),fs=new Set(),ls=new Set(),unknownFamUsed=false;
            data.forEach(function(r){
                if(r.category)cs.add(r.category);
                /* Derive layers from category mapping */
                var layer=CLL[r.category];
                if(layer)ls.add(layer);
                (r.relationships||[]).forEach(function(rel){
                    var fam=rel.relationshipFamily;
                    if(fam){fs.add(fam)}else{unknownFamUsed=true}
                })
            });
            CL=Array.from(cs).sort();FL=Array.from(fs).sort();LL=Array.from(ls).sort();
            if(unknownFamUsed&&FL.indexOf('unknown')===-1){FL.push('unknown')}
            CL.forEach(function(c,i){CC[c]=CP[i%CP.length];CS[c]=SC[i%SC.length];CLB[c]=friendlyLabel(c)});
            FL.forEach(function(f,i){FC[f]=FP[i%FP.length];FLB[f]=FLM[f]||friendlyLabel(f)});
            LL.forEach(function(l,i){LC[l]=LPC[l]||'#888';LLB[l]=l});
            /* Merge default TFM with data-derived overrides */
            TFM={};for(var k in TFM_DEFAULT)TFM[k]=TFM_DEFAULT[k];
            data.forEach(function(r){(r.relationships||[]).forEach(function(rel){if(rel.relationshipType&&rel.relationshipFamily)TFM[rel.relationshipType]=rel.relationshipFamily})});
            aCats=new Set(CL);aFams=new Set(FL);aLayers=new Set(LL)
        }

        /* ═══════ SIMULATION CONSTANTS ═══════ */
        var REP=280,SL=110,SS=0.012,CC2=0.005,CG=0.008,DMP=0.65,AS=0.006,DR=0.88;
        var nodes=[],gE=[],nM={};
        var alpha=1,curProj='default';
        var cam={x:0,y:0,z:1},camTgt=null;
        var hovN=null,pinN=null,dragN=null,selN=null;
        var isPan=false,panS={x:0,y:0};
        var mS={x:-9999,y:-9999},wM={x:-9999,y:-9999};
        var catC={};var fc=0,lt=performance.now(),fps=0;
        var minY=Infinity,maxY=-Infinity,maxIL=1;
        var chordHC=null;var cNC={};
        var tR={min:-Infinity,max:Infinity};var tRF={min:0,max:0};
        var pCache={};var dLoaded=false;
        var ddOpen=false,kbFI=-1,fRes=[];
        var canvas=document.getElementById('graph-canvas'),ctx=canvas.getContext('2d');
        var mmC=document.getElementById('minimap-canvas'),mmX=mmC.getContext('2d');
        var W=0,H=0;
        var umapK=0;
        var bipG={left:[],right:[],mid:[]};
        var wasChord=false;

        /* ═══════ CANVAS TOAST ═══════ */
        var toastNode=null,toastStart=0;
        var TOAST_IN=450,TOAST_STAY=4500,TOAST_OUT=900;
        function triggerToast(nd){toastNode=nd;toastStart=performance.now()}

        function drawToast(){
            if(!toastNode)return;
            if(!toastNode.visible){toastNode=null;return}
            var elapsed=performance.now()-toastStart;
            var total=TOAST_IN+TOAST_STAY+TOAST_OUT;
            if(elapsed>total){toastNode=null;return}
            var opacity;
            if(elapsed<TOAST_IN)opacity=elapsed/TOAST_IN;
            else if(elapsed<TOAST_IN+TOAST_STAY)opacity=1;
            else opacity=1-(elapsed-TOAST_STAY-TOAST_IN)/TOAST_OUT;
            opacity=Math.max(0,Math.min(1,opacity));
            var sp=w2s(toastNode.x,toastNode.y);
            var name=toastNode.name;
            var col=CC[toastNode.category]||'#48e8d8';
            ctx.save();ctx.globalAlpha=opacity;
            ctx.font='600 11.5px Inter';
            var tw=ctx.measureText(name).width;
            var padX=16,padY=9,dotSpace=10;
            var bw=tw+padX*2+dotSpace,bh=32,arrowH=7;
            var baseR=Math.max(3,(5+toastNode.degree*0.6))*cam.z;
            baseR=Math.max(3,Math.min(baseR,28));
            var bx=sp.x-bw/2,by=sp.y-baseR-16-bh-arrowH;
            bx=clamp(bx,10,W-bw-10);by=clamp(by,10,H-bh-arrowH-10);
            ctx.shadowColor='rgba(0,0,0,0.5)';ctx.shadowBlur=20;ctx.shadowOffsetY=4;
            drawRoundRect(ctx,bx,by,bw,bh,8);ctx.fillStyle='rgba(12,13,22,0.92)';ctx.fill();
            ctx.shadowColor='transparent';ctx.shadowBlur=0;ctx.shadowOffsetY=0;
            ctx.strokeStyle=hexToRGBA(col,0.5);ctx.lineWidth=1;ctx.stroke();
            ctx.beginPath();ctx.arc(bx+padX,by+bh/2,3.5,0,Math.PI*2);ctx.fillStyle=col;ctx.fill();
            var dGrd=ctx.createRadialGradient(bx+padX,by+bh/2,1,bx+padX,by+bh/2,10);
            dGrd.addColorStop(0,hexToRGBA(col,0.25));dGrd.addColorStop(1,hexToRGBA(col,0));
            ctx.fillStyle=dGrd;ctx.beginPath();ctx.arc(bx+padX,by+bh/2,10,0,Math.PI*2);ctx.fill();
            ctx.fillStyle='#e8eaf2';ctx.textAlign='left';ctx.textBaseline='middle';
            ctx.fillText(name,bx+padX+dotSpace,by+bh/2+0.5);
            var arrowX=clamp(sp.x,bx+10,bx+bw-10);
            ctx.beginPath();ctx.moveTo(arrowX-6,by+bh);ctx.lineTo(arrowX,by+bh+arrowH);ctx.lineTo(arrowX+6,by+bh);ctx.closePath();
            ctx.fillStyle='rgba(12,13,22,0.92)';ctx.fill();
            ctx.strokeStyle=hexToRGBA(col,0.5);ctx.lineWidth=1;
            ctx.beginPath();ctx.moveTo(arrowX-6,by+bh);ctx.lineTo(arrowX,by+bh+arrowH);ctx.lineTo(arrowX+6,by+bh);ctx.stroke();
            ctx.beginPath();ctx.setLineDash([2,3]);ctx.moveTo(arrowX,by+bh+arrowH);ctx.lineTo(sp.x,sp.y-baseR-4);
            ctx.strokeStyle=hexToRGBA(col,0.18);ctx.lineWidth=0.8;ctx.stroke();ctx.setLineDash([]);
            ctx.globalAlpha=1;ctx.restore()
        }

        /* ═══════ AMBIENT BLOBS ═══════ */
        var ambBlobs=[];
        function initAmbBlobs(){
            ambBlobs=[];var cols=['#48e8d8','#C9A44e','#7BE0A0','#8B7BF0','#45B7D1'];
            for(var i=0;i<5;i++){ambBlobs.push({x:Math.random()*2000,y:Math.random()*2000,r:Math.random()*280+140,vx:(Math.random()-0.5)*0.12,vy:(Math.random()-0.5)*0.08,color:cols[i],opacity:Math.random()*0.022+0.008})}
        }
        function drawAmbBlobs(){
            ambBlobs.forEach(function(b){b.x+=b.vx;b.y+=b.vy;
                if(b.x<-b.r)b.x=W+b.r;if(b.x>W+b.r)b.x=-b.r;
                if(b.y<-b.r)b.y=H+b.r;if(b.y>H+b.r)b.y=-b.r;
                var grd=ctx.createRadialGradient(b.x,b.y,0,b.x,b.y,b.r);
                grd.addColorStop(0,hexToRGBA(b.color,b.opacity));grd.addColorStop(1,hexToRGBA(b.color,0));
                ctx.fillStyle=grd;ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,Math.PI*2);ctx.fill()})
        }

        /* ═══════ DUST PARTICLES ═══════ */
        var dustParts=[];
        function initDust(){
            dustParts=[];for(var i=0;i<35;i++){dustParts.push({x:Math.random()*2000,y:Math.random()*2000,size:Math.random()*1.2+0.3,speed:Math.random()*0.2+0.04,angle:Math.random()*Math.PI*2,opacity:Math.random()*0.12+0.025,drift:Math.random()*0.003-0.0015})}
        }
        function drawDust(){
            dustParts.forEach(function(p){p.x+=Math.cos(p.angle)*p.speed;p.y+=Math.sin(p.angle)*p.speed;p.angle+=p.drift;
                if(p.x<-10)p.x=W+10;if(p.x>W+10)p.x=-10;if(p.y<-10)p.y=H+10;if(p.y>H+10)p.y=-10;
                ctx.beginPath();ctx.arc(p.x,p.y,p.size,0,Math.PI*2);ctx.fillStyle=hexToRGBA('#8892b0',p.opacity);ctx.fill()})
        }

        /* ═══════ VIEW HELPERS ═══════ */
        function uPS(){var p=document.getElementById('projection-chips'),a=p.querySelector('.proj-chip.active');if(a){p.style.setProperty('--pill-left',a.offsetLeft+'px');p.style.setProperty('--pill-width',a.offsetWidth+'px')}}
        function sPC(pj){pCache[pj]=nodes.map(function(n){return{id:n.id,x:n.x,y:n.y}})}
        function rPC(pj){var c=pCache[pj];if(!c)return false;var m={};c.forEach(function(v){m[v.id]=v});nodes.forEach(function(n){if(m[n.id]){n.x=m[n.id].x;n.y=m[n.id].y}});return true}
        function sCV(){var r=canvas.parentElement.getBoundingClientRect();W=r.width;H=r.height;canvas.width=W*devicePixelRatio;canvas.height=H*devicePixelRatio;ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0)}
        function resize(){sCV();if(dLoaded){rCC();rLC();if(curProj!=='chord')fCam()}uPS()}

        function fCam(){var v=nodes.filter(function(n){return n.visible});if(!v.length)return;var x1=Infinity,x2=-Infinity,y1=Infinity,y2=-Infinity;var ut=curProj!=='default'&&curProj!=='chord';v.forEach(function(n){var px=ut&&n.targetX!==undefined?n.targetX:n.x;var py=ut&&n.targetY!==undefined?n.targetY:n.y;if(px<x1)x1=px;if(px>x2)x2=px;if(py<y1)y1=py;if(py>y2)y2=py});if(x1===Infinity)return;var p=120,gw=x2-x1+p*2,gh=y2-y1+p*2,z=Math.min(W/gw,H/gh,1.2);cam.z=z;cam.x=W/2-((x1+x2)/2)*z;cam.y=H/2-((y1+y2)/2)*z;camTgt=null}

        function pTN(nd){if(!nd)return;var tz=Math.max(cam.z,1.2);camTgt={x:W/2-nd.x*tz,y:H/2-nd.y*tz,z:tz}}
        function uCP(){if(!camTgt)return;var dx=camTgt.x-cam.x,dy=camTgt.y-cam.y,dz=camTgt.z-cam.z;if(Math.abs(dx)<.3&&Math.abs(dy)<.3&&Math.abs(dz)<.001){cam.x=camTgt.x;cam.y=camTgt.y;cam.z=camTgt.z;camTgt=null;return}cam.x+=dx*.09;cam.y+=dy*.09;cam.z+=dz*.09}
        function reheatAlpha(){alpha=1}

        /* ═══════ UMAP EMBEDDING ═══════ */
        function fitAB(minDist){
            if(Math.abs(minDist-0.1)<0.01)return{a:1.577,b:0.895};
            if(minDist<0.01)return{a:1.0,b:1.0};
            var bestA=1,bestB=1,bestErr=Infinity;
            for(var a=0.2;a<8;a+=0.15){for(var b=0.2;b<3;b+=0.05){var u=minDist*minDist;var q=1/(1+a*Math.pow(u,b));var err=Math.abs(q-0.001);if(err<bestErr){bestErr=err;bestA=a;bestB=b}}}
            return{a:bestA,b:bestB}
        }

        function computeUMAP(){
            var vis=nodes.filter(function(n){return n.visible});var n=vis.length;
            if(n<3){vis.forEach(function(nd){nd.targetX=W/2;nd.targetY=H/2});umapK=0;return}
            umapK=Math.min(15,Math.max(2,Math.floor(Math.sqrt(n))));
            var maxDeg=Math.max(1,nodes.reduce(function(a,n){return Math.max(a,n.degree)},0));
            var dim=4+CL.length;
            var feats=vis.map(function(nd){var fv=new Array(dim).fill(0);fv[0]=nd.confidence||0;fv[1]=nd.degree/maxDeg;fv[2]=(nd.inheritanceLevel||0)/Math.max(1,maxIL);fv[3]=0.5;var ci=CL.indexOf(nd.category);if(ci>=0)fv[4+ci]=1;return fv});
            var dist=Array.from({length:n},function(){return new Array(n).fill(0)});
            for(var i=0;i<n;i++){for(var j=i+1;j<n;j++){var dd=0;for(var k=0;k<dim;k++){var df=feats[i][k]-feats[j][k];dd+=df*df}dd=Math.sqrt(Math.max(1e-12,dd));dist[i][j]=dd;dist[j][i]=dd}}
            var knnI=new Array(n);
            for(var i=0;i<n;i++){var nb=[];for(var j=0;j<n;j++){if(i!==j)nb.push({j:j,d:dist[i][j]})}nb.sort(function(a,b){return a.d-b.d});knnI[i]=nb.slice(0,umapK).map(function(x){return x.j})}
            var targetE=Math.log2(umapK);var sigmas=new Array(n),rhos=new Array(n);
            for(var i=0;i<n;i++){rhos[i]=dist[i][knnI[i][0]];var lo=1e-5,hi=1e4;for(var it=0;it<64;it++){var mid=(lo+hi)/2,ent=0;for(var jj=0;jj<knnI[i].length;jj++){var dv=dist[i][knnI[i][jj]]-rhos[i];var p=dv<=0?1:Math.exp(-dv/mid);if(p>1e-15)ent-=p*Math.log2(p)}if(ent<targetE)lo=mid;else hi=mid}sigmas[i]=(lo+hi)/2}
            var P=new Array(n);for(var i=0;i<n;i++)P[i]={};
            for(var i=0;i<n;i++){for(var jj=0;jj<knnI[i].length;jj++){var j=knnI[i][jj];var dv=dist[i][j]-rhos[i];P[i][j]=dv<=0?1:Math.exp(-dv/sigmas[i])}}
            var Ps=new Array(n);for(var i=0;i<n;i++)Ps[i]={};
            for(var i=0;i<n;i++){for(var j in P[i]){var pij=P[i][j];var pji=(P[j]&&P[j][i])||0;var sym=pij+pji-pij*pji;if(sym>1e-10)Ps[i][j]=sym}}
            for(var i=0;i<n;i++){var rs=0;for(var j in Ps[i])rs+=Ps[i][j];if(rs>1e-12)for(var j in Ps[i])Ps[i][j]/=rs}
            var edges=[];
            for(var i=0;i<n;i++){for(var j in Ps[i]){var ji=parseInt(j);if(ji>i)edges.push({s:i,t:ji,w:Ps[i][j]})}}
            var ab=fitAB(0.1);var ua=ab.a,ub=ab.b;
            var emb=new Array(n);for(var i=0;i<n;i++){var ang=(i/n)*Math.PI*2;var rad=0.5+Math.random()*0.5;emb[i]=[Math.cos(ang)*rad,Math.sin(ang)*rad]}
            var nEpochs=Math.min(500,Math.max(200,n*10));var negRate=5,lr0=1.0;
            for(var epoch=0;epoch<nEpochs;epoch++){
                var alpha=lr0*(1-epoch/nEpochs);alpha=Math.max(alpha,0.001);
                for(var i=edges.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var tmp=edges[i];edges[i]=edges[j];edges[j]=tmp}
                for(var e=0;e<edges.length;e++){
                    var src=edges[e].s,tgt=edges[e].t,w=edges[e].w;
                    for(var s=0;s<=negRate;s++){
                        var ntgt=s===0?tgt:Math.floor(Math.random()*n);
                        var dx=emb[src][0]-emb[ntgt][0],dy=emb[src][1]-emb[ntgt][1];
                        var dSq=dx*dx+dy*dy;if(dSq<1e-12)dSq=1e-12;
                        var q=1/(1+ua*Math.pow(dSq,ub));
                        if(s===0){var gf=-2*ub*w*q/(dSq+1e-8);emb[src][0]+=alpha*gf*dx;emb[src][1]+=alpha*gf*dy;emb[tgt][0]-=alpha*gf*dx;emb[tgt][1]-=alpha*gf*dy}
                        else{if(Ps[src]&&Ps[src][ntgt])continue;var gf2=2*ub*q/(1-q+1e-10);emb[src][0]+=alpha*gf2*dx;emb[src][1]+=alpha*gf2*dy}
                    }
                }
            }
            var xs=emb.map(function(e){return e[0]}),ys=emb.map(function(e){return e[1]});
            var xMin=Math.min.apply(null,xs),xMax=Math.max.apply(null,xs);
            var yMin=Math.min.apply(null,ys),yMax=Math.max.apply(null,ys);
            var xR=Math.max(.001,xMax-xMin),yR=Math.max(.001,yMax-yMin);
            var pad=160,scl=Math.min((W-2*pad)/xR,(H-2*pad)/yR);
            var cx2=W/2-(xMin+xMax)/2*scl,cy2=H/2-(yMin+yMax)/2*scl;
            var golden=2.399963;
            vis.forEach(function(nd,i){nd.targetX=cx2+emb[i][0]*scl+Math.cos(i*golden)*8;nd.targetY=cy2+emb[i][1]*scl+Math.sin(i*golden)*8})
        }

        /* ═══════ SPECTRAL LAYOUT ═══════ */
        function computeSpectral(){
            var vis=nodes.filter(function(n){return n.visible});var n=vis.length;
            if(n<3){vis.forEach(function(nd){nd.targetX=W/2;nd.targetY=H/2});return}
            var idx={};vis.forEach(function(nd,i){idx[nd.id]=i});
            var deg=new Array(n).fill(0);var nb=[];for(var i=0;i<n;i++)nb[i]=[];
            gE.forEach(function(e){var si=idx[e.source],ti=idx[e.target];if(si===undefined||ti===undefined||si===ti)return;if(nb[si].indexOf(ti)===-1){nb[si].push(ti);deg[si]++}if(nb[ti].indexOf(si)===-1){nb[ti].push(si);deg[ti]++}});
            var maxD=Math.max.apply(null,deg.concat([1]))+1;
            var eigs=[];
            for(var ev=0;ev<2;ev++){
                var v=new Array(n);for(var i=0;i<n;i++)v[i]=Math.random()-.5;
                var vn=Math.sqrt(v.reduce(function(a,b){return a+b*b},0));if(vn<1e-12)vn=1e-12;for(var i=0;i<n;i++)v[i]/=vn;
                for(var it=0;it<500;it++){
                    var nv=new Array(n).fill(0);
                    for(var i=0;i<n;i++){nv[i]=(maxD-deg[i])*v[i];for(var j=0;j<nb[i].length;j++)nv[i]+=v[nb[i][j]]}
                    if(ev===0){var mean=0;for(var i=0;i<n;i++)mean+=nv[i];mean/=n;for(var i=0;i<n;i++)nv[i]-=mean}
                    else{var dot=0;for(var i=0;i<n;i++)dot+=nv[i]*eigs[0][i];for(var i=0;i<n;i++)nv[i]-=dot*eigs[0][i]}
                    var nvn=Math.sqrt(nv.reduce(function(a,b){return a+b*b},0));if(nvn<1e-12)break;for(var i=0;i<n;i++)v[i]=nv[i]/nvn
                }
                eigs.push(v.slice())
            }
            var xs=eigs[0],ys=eigs[1];
            var xMin=Math.min.apply(null,xs),xMax=Math.max.apply(null,xs);
            var yMin=Math.min.apply(null,ys),yMax=Math.max.apply(null,ys);
            var xR=Math.max(.001,xMax-xMin),yR=Math.max(.001,yMax-yMin);
            var pad=160,scl=Math.min((W-2*pad)/xR,(H-2*pad)/yR);
            var cx2=W/2-(xMin+xMax)/2*scl,cy2=H/2-(yMin+yMax)/2*scl;
            vis.forEach(function(nd,i){nd.targetX=cx2+xs[i]*scl;nd.targetY=cy2+ys[i]*scl})
        }

        /* ═══════ BIPARTITE PROJECTION ═══════ */
        function computeBipartite(){
            var vis=nodes.filter(function(n){return n.visible});
            bipG={left:[],right:[],mid:[]};
            vis.forEach(function(nd){var l=nd.layer;
                if(BIP_LEFT.indexOf(l)>=0)bipG.left.push(nd);
                else if(BIP_RIGHT.indexOf(l)>=0)bipG.right.push(nd);
                else bipG.mid.push(nd)
            });
            bipG.left.sort(function(a,b){return shortLabel(a.category).localeCompare(shortLabel(b.category))});
            bipG.right.sort(function(a,b){return shortLabel(b.category).localeCompare(shortLabel(a.category))});
            bipG.mid.sort(function(a,b){return a.y-b.y});
            var padY=80;var leftX=W*0.22,rightX=W*0.78;var availH=H-padY*2;
            bipG.left.forEach(function(nd,i){nd.targetX=leftX+(Math.random()-.5)*30;nd.targetY=padY+(i+.5)*(availH/Math.max(1,bipG.left.length))});
            bipG.right.forEach(function(nd,i){nd.targetX=rightX+(Math.random()-.5)*30;nd.targetY=padY+(i+.5)*(availH/Math.max(1,bipG.right.length))});
            bipG.mid.forEach(function(nd,i){nd.targetX=W/2+(Math.random()-.5)*40;nd.targetY=padY+(i+.5)*(availH/Math.max(1,bipG.mid.length))})
        }

        /* ═══════ PROJECTION DISPATCH ═══════ */
        function applyProjection(pj){
            var vis=nodes.filter(function(n){return n.visible});if(!vis.length)return;
            try{switch(pj){
                case'category':projCategory(vis);break;case'layer':projLayer(vis);break;
                case'confidence':projConfidence(vis);break;case'radial':projRadial(vis);break;
                case'umap':computeUMAP();break;case'spectral':computeSpectral();break;
                case'bipartite':computeBipartite();break;default:break
            }}catch(err){console.warn('Projection error:',err)}
        }
        function projCategory(vis){
            var cats={};vis.forEach(function(n){if(!cats[n.category])cats[n.category]=[];cats[n.category].push(n)});
            var keys=Object.keys(cats),nk=keys.length;if(!nk)return;
            var cx=W/2,cy=H/2,rad=Math.min(W,H)*0.32;
            keys.forEach(function(k,i){var ang=(i/nk)*Math.PI*2-Math.PI/2;var ccx=cx+Math.cos(ang)*rad,ccy=cy+Math.sin(ang)*rad;var arr=cats[k];var sr=Math.max(22,Math.min(90,14*Math.sqrt(arr.length)));arr.forEach(function(nd,j){var a2=(j/arr.length)*Math.PI*2;var r2=sr*(.35+.65*((j%3)+1)/3);nd.targetX=ccx+Math.cos(a2)*r2;nd.targetY=ccy+Math.sin(a2)*r2})})
        }
        function projLayer(vis){
            var layers={};vis.forEach(function(n){var l=n.layer||'Unknown';if(!layers[l])layers[l]=[];layers[l].push(n)});
            var keys=Object.keys(layers).sort(),nk=keys.length;if(!nk)return;
            var padX=180,padY=100,gap=(H-2*padY)/Math.max(1,nk);
            keys.forEach(function(k,i){var arr=layers[k],cy=padY+gap*(i+.5);var totalW=Math.min(W-2*padX,arr.length*55);arr.forEach(function(nd,j){nd.targetX=padX+(j+.5)*(totalW/arr.length);nd.targetY=cy+(Math.random()-.5)*gap*0.25})})
        }
        function projConfidence(vis){
            var pad=160;var sorted=vis.slice().sort(function(a,b){return(a.confidence||0.5)-(b.confidence||0.5)});
            var golden=2.399963;
            sorted.forEach(function(nd,i){nd.targetX=pad+(nd.confidence||0.5)*(W-2*pad);nd.targetY=H/2+Math.sin(i*golden)*H*0.35})
        }
        function projRadial(vis){
            var cx=W/2,cy=H/2,rad=Math.min(W,H)*0.35;
            var maxDeg=Math.max(1,nodes.reduce(function(a,n){return Math.max(a,n.degree)},0));
            var sorted=vis.slice().sort(function(a,b){return a.degree-b.degree});
            sorted.forEach(function(nd,i){var ang=(i/sorted.length)*Math.PI*2;var r2=rad*(0.2+0.8*(nd.degree/maxDeg));nd.targetX=cx+Math.cos(ang)*r2;nd.targetY=cy+Math.sin(ang)*r2})
        }

        /* ═══════ FILTERING ═══════ */
        function uFilt(){
            var vc=0;
            nodes.forEach(function(n){
                var inCat=aCats.has(n.category);
                var inLay=aLayers.has(n.layer);
                var inTime=isFiniteNum(n.year)?n.year>=tR.min&&n.year<=tR.max:true;
                n.visible=inCat&&inLay&&inTime;
                if(n.visible)vc++
            });
            cNC={};nodes.forEach(function(n){if(n.visible){if(!cNC[n.category])cNC[n.category]=0;cNC[n.category]++}});
            gE.forEach(function(e){
                var s=nM[e.source],t=nM[e.target];
                var famOk=e.family==='unknown'||aFams.has(e.family);
                e.visible=s&&t&&s.visible&&t.visible&&famOk
            });
            document.getElementById('empty-state').classList.toggle('visible',vc===0);
            document.getElementById('time-visible-count').textContent=vc;
            document.getElementById('hud-v').textContent=vc;
            var ec=gE.filter(function(e){return e.visible}).length;
            document.getElementById('hud-e').textContent=ec;
            if(curProj!=='default'&&curProj!=='chord'){applyProjection(curProj)}
            rCC();if(curProj==='default')reheatAlpha()
        }
        function rCC(){CL.forEach(function(c){var el=document.getElementById('ctog-'+c);if(el){var cnt=cNC[c]||0;el.querySelector('.node-count').textContent=cnt;el.classList.toggle('disabled',cnt===0)}})}
        function rLC(){
            var grp=document.getElementById('layer-group');
            if(!LL.length){grp.style.display='none';return}
            grp.style.display='';var html='';
            LL.forEach(function(l){var cnt=nodes.filter(function(n){return n.layer===l&&n.visible}).length;
                html+='<label class="toggle-item" data-layer="'+l+'"><input type="checkbox" checked><span class="checkmark"></span><span class="cat-dot" style="background:'+LC[l]+'"></span><span>'+l+'</span><span class="node-count">'+cnt+'</span></label>'
            });
            document.getElementById('layer-toggles').innerHTML=html;
            document.getElementById('layer-toggles').querySelectorAll('.toggle-item').forEach(function(el){
                el.querySelector('input').addEventListener('change',function(){var l=el.dataset.layer;if(this.checked)aLayers.add(l);else aLayers.delete(l);uFilt()})
            })
        }

        /* ═══════ FORCE SIMULATION ═══════ */
        function simTick(){
            if(curProj!=='default')return;
            var vis=nodes.filter(function(n){return n.visible});if(!vis.length)return;
            alpha*=0.998;if(alpha<0.003)alpha=0.003;
            var i,j,n=vis.length;
            for(i=0;i<n;i++){var a=vis[i];if(a===dragN)continue;var fx=0,fy=0;
                for(j=0;j<n;j++){if(i===j)continue;var b=vis[j];var dx=a.x-b.x,dy=a.y-b.y,d2=dx*dx+dy*dy;if(d2<1)d2=1;var d=Math.sqrt(d2);if(d<REP){var f=(REP-d)/d*SS*alpha;fx+=dx*f;fy+=dy*f}}
                a.vx=(a.vx||0)+fx;a.vy=(a.vy||0)+fy
            }
            var cxs={},cys={},ccs={};
            vis.forEach(function(nd){var c=nd.category;if(!cxs[c]){cxs[c]=0;cys[c]=0;ccs[c]=0}cxs[c]+=nd.x;cys[c]+=nd.y;ccs[c]++});
            vis.forEach(function(nd){var c=nd.category,cnt=Math.max(1,ccs[c]||1);var ccx=cxs[c]/cnt,ccy=cys[c]/cnt;nd.vx=(nd.vx||0)+(ccx-nd.x)*CC2*alpha;nd.vy=(nd.vy||0)+(ccy-nd.y)*CC2*alpha});
            vis.forEach(function(nd){if(nd===dragN)return;nd.vx=(nd.vx||0)*CG;nd.vy=(nd.vy||0)*CG});
            gE.forEach(function(e){if(!e.visible)return;var s=nM[e.source],t=nM[e.target];if(!s||!t)return;var dx=t.x-s.x,dy=t.y-s.y,d=Math.sqrt(dx*dx+dy*dy);if(d<1)return;var f=(d-SL)/d*AS*alpha;
                if(s!==dragN){s.vx=(s.vx||0)+dx*f;s.vy=(s.vy||0)+dy*f}
                if(t!==dragN){t.vx=(t.vx||0)-dx*f;t.vy=(t.vy||0)-dy*f}
            });
            vis.forEach(function(nd){if(nd===dragN)return;nd.vx=(nd.vx||0)*DR;nd.vy=(nd.vy||0)*DR;var spd=Math.sqrt(nd.vx*nd.vx+nd.vy*nd.vy);if(spd>50){nd.vx=nd.vx/spd*50;nd.vy=nd.vy/spd*50}nd.x+=nd.vx;nd.y+=nd.vy;
                if(!isFiniteNum(nd.x)||!isFiniteNum(nd.y)){nd.x=(Math.random()-.5)*100;nd.y=(Math.random()-.5)*100;nd.vx=0;nd.vy=0}
            })
        }

        /* ═══════ STRUCTURED PROJECTION INTERPOLATION ═══════ */
        function interpTick(){
            if(curProj==='default'||curProj==='chord')return;
            var vis=nodes.filter(function(n){return n.visible});var rate=0.1;
            vis.forEach(function(nd){if(nd===dragN)return;if(nd.targetX===undefined||nd.targetY===undefined)return;
                nd.x+=(nd.targetX-nd.x)*rate;nd.y+=(nd.targetY-nd.y)*rate;
                if(!isFiniteNum(nd.x))nd.x=nd.targetX;if(!isFiniteNum(nd.y))nd.y=nd.targetY
            })
        }

        /* ═══════ DRAWING ═══════ */
        function w2s(wx,wy){return{x:wx*cam.z+cam.x,y:wy*cam.z+cam.y}}
        function s2w(sx,sy){return{x:(sx-cam.x)/cam.z,y:(sy-cam.y)/cam.z}}

        function drawShape(x,y,r,shape){
            r=Math.max(1,r);
            switch(shape){
                case'triangle':ctx.beginPath();ctx.moveTo(x,y-r);ctx.lineTo(x-r*.866,y+r*.5);ctx.lineTo(x+r*.866,y+r*.5);ctx.closePath();break;
                case'square':ctx.beginPath();var s=r*.82;ctx.rect(x-s,y-s,s*2,s*2);break;
                case'diamond':ctx.beginPath();ctx.moveTo(x,y-r);ctx.lineTo(x+r*.7,y);ctx.lineTo(x,y+r);ctx.lineTo(x-r*.7,y);ctx.closePath();break;
                case'hexagon':ctx.beginPath();for(var i=0;i<6;i++){var a=i*Math.PI/3-Math.PI/6;ctx.lineTo(x+Math.cos(a)*r,y+Math.sin(a)*r)}ctx.closePath();break;
                default:ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);break
            }
        }

        function drawEdges(){
            var showFlow=document.getElementById('lens-flow').checked;
            var showHeat=document.getElementById('lens-heatmap').checked;
            var isBip=curProj==='bipartite';
            gE.forEach(function(e){
                if(!e.visible)return;var s=nM[e.source],t=nM[e.target];if(!s||!t)return;
                var sp=w2s(s.x,s.y),tp=w2s(t.x,t.y);
                if(sp.x<-50&&tp.x<-50)return;if(sp.x>W+50&&tp.x>W+50)return;
                if(sp.y<-50&&tp.y<-50)return;if(sp.y>H+50&&tp.y>H+50)return;
                var isHov=hovN&&(hovN.id===e.source||hovN.id===e.target);
                var isSel=selN&&(selN.id===e.source||selN.id===e.target);
                var isPin=pinN&&(pinN.id===e.source||pinN.id===e.target);
                var famC=FC[e.family]||'#48e8d8';
                var highlight=isHov||isSel||isPin;
                var baseA=highlight?0.3:0.07;
                ctx.strokeStyle=hexToRGBA(famC,baseA);ctx.lineWidth=highlight?1.4:0.6;
                if(isBip){
                    ctx.beginPath();ctx.moveTo(sp.x,sp.y);var mx=(sp.x+tp.x)/2,my=(sp.y+tp.y)/2;ctx.quadraticCurveTo(mx,my,tp.x,tp.y);ctx.stroke()
                }else{
                    if(showFlow&&curProj!=='chord'){
                        var dx=tp.x-sp.x,dy=tp.y-sp.y,d=Math.sqrt(dx*dx+dy*dy);
                        if(d>10){var nx=-dy/d,ny=dx/d;var cpx=(sp.x+tp.x)/2+nx*d*0.08,cpy=(sp.y+tp.y)/2+ny*d*0.08;
                            ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.quadraticCurveTo(cpx,cpy,tp.x,tp.y);ctx.stroke();
                            if(highlight){var gt=0.4+0.3*Math.sin(performance.now()*0.003);var grd=ctx.createLinearGradient(sp.x,sp.y,tp.x,tp.y);grd.addColorStop(0,hexToRGBA(famC,0));grd.addColorStop(0.5,hexToRGBA(famC,gt));grd.addColorStop(1,hexToRGBA(famC,0));ctx.strokeStyle=grd;ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.quadraticCurveTo(cpx,cpy,tp.x,tp.y);ctx.stroke()}
                        }else{ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.lineTo(tp.x,tp.y);ctx.stroke()}
                    }else{ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.lineTo(tp.x,tp.y);ctx.stroke()}
                }
                if(showHeat&&e.family==='GOVERNANCE'){ctx.strokeStyle=hexToRGBA('#E06070',0.09);ctx.lineWidth=3.5;ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.lineTo(tp.x,tp.y);ctx.stroke()}
            })
        }

        function drawHulls(){
            if(!document.getElementById('lens-hulls').checked)return;
            if(SP.indexOf(curProj)>=0)return;if(curProj==='chord')return;
            Object.keys(catC).forEach(function(cat){
                var pts=catC[cat];if(pts.length<3)return;
                var sPts=pts.map(function(p){return w2s(p.x,p.y)});
                var cx=0,cy=0;sPts.forEach(function(p){cx+=p.x;cy+=p.y});cx/=sPts.length;cy/=sPts.length;
                sPts.sort(function(a,b){return Math.atan2(a.y-cy,a.x-cx)-Math.atan2(b.y-cy,b.x-cx)});
                ctx.beginPath();ctx.moveTo(sPts[0].x,sPts[0].y);
                for(var i=1;i<sPts.length;i++)ctx.lineTo(sPts[i].x,sPts[i].y);ctx.closePath();
                var hullCol=CC[cat]||'#888';
                var hgrd=ctx.createRadialGradient(cx,cy,0,cx,cy,Math.max(100,Math.sqrt((cx-sPts[0].x)**2+(cy-sPts[0].y)**2)));
                hgrd.addColorStop(0,hexToRGBA(hullCol,0.025));hgrd.addColorStop(1,hexToRGBA(hullCol,0.005));
                ctx.fillStyle=hgrd;ctx.fill();ctx.strokeStyle=hexToRGBA(hullCol,0.08);ctx.lineWidth=1;ctx.stroke()
            })
        }

        function drawNodes(){
            var showCent=document.getElementById('lens-centrality').checked;
            var showConfCol=document.getElementById('lens-confidence-color').checked;
            var showObs=document.getElementById('lens-observability').checked;
            var maxDeg=Math.max(1,nodes.reduce(function(a,n){return Math.max(a,n.degree)},0));
            nodes.forEach(function(nd){
                if(!nd.visible)return;var sp=w2s(nd.x,nd.y);
                if(sp.x<-40||sp.x>W+40||sp.y<-40||sp.y>H+40)return;
                var isHov=hovN&&hovN.id===nd.id;var isSel=selN&&selN.id===nd.id;var isPin=pinN&&pinN.id===nd.id;
                var baseR=4.5+nd.degree*0.55;if(showCent)baseR=3.5+nd.degree*1.3;
                var r=Math.max(2.5,baseR)*cam.z;r=Math.max(2,Math.min(r,24));
                if(isHov)r*=1.35;
                var col=showConfCol?confidenceColor(nd.confidence):(CC[nd.category]||'#888');
                var alpha2=1;
                /* Confidence-based ghosting (replaces observability) */
                if(showObs){var c=nd.confidence||0.7;if(c<0.4)alpha2=0.15;else if(c<0.65)alpha2=0.45}
                if(isHov||isSel||isPin)alpha2=1;
                ctx.globalAlpha=alpha2;
                if(isHov||isSel||isPin){
                    var glowCol=isSel?'#48e8d8':isPin?'#C9A44e':'#ffffff';
                    var glowR=r+8;var gGrd=ctx.createRadialGradient(sp.x,sp.y,r*0.5,sp.x,sp.y,glowR);
                    gGrd.addColorStop(0,hexToRGBA(glowCol,0.18));gGrd.addColorStop(1,hexToRGBA(glowCol,0));
                    ctx.fillStyle=gGrd;ctx.beginPath();ctx.arc(sp.x,sp.y,glowR,0,Math.PI*2);ctx.fill()
                }
                var ambGrd=ctx.createRadialGradient(sp.x,sp.y,r*0.2,sp.x,sp.y,r+3);
                ambGrd.addColorStop(0,hexToRGBA(col,0.12));ambGrd.addColorStop(1,hexToRGBA(col,0));
                ctx.fillStyle=ambGrd;ctx.beginPath();ctx.arc(sp.x,sp.y,r+3,0,Math.PI*2);ctx.fill();
                var nGrd=ctx.createRadialGradient(sp.x-r*0.25,sp.y-r*0.25,0,sp.x,sp.y,r);
                nGrd.addColorStop(0,hexToRGBA(col,1));nGrd.addColorStop(1,hexToRGBA(col,0.75));
                ctx.fillStyle=nGrd;drawShape(sp.x,sp.y,r,CS[nd.category]||'circle');ctx.fill();
                ctx.fillStyle=hexToRGBA('#ffffff',0.15);ctx.beginPath();ctx.arc(sp.x-r*0.2,sp.y-r*0.2,r*0.35,0,Math.PI*2);ctx.fill();
                if(isHov){ctx.strokeStyle=hexToRGBA('#ffffff',0.35);ctx.lineWidth=1.2;drawShape(sp.x,sp.y,r+2.5,CS[nd.category]||'circle');ctx.stroke()}
                if(isSel){ctx.strokeStyle=hexToRGBA('#48e8d8',0.5);ctx.lineWidth=1.2;drawShape(sp.x,sp.y,r+3,CS[nd.category]||'circle');ctx.stroke()}
                if(isPin){ctx.strokeStyle=hexToRGBA('#C9A44e',0.4);ctx.lineWidth=1;ctx.setLineDash([3,3]);drawShape(sp.x,sp.y,r+4,CS[nd.category]||'circle');ctx.stroke();ctx.setLineDash([])}
                ctx.shadowColor='transparent';ctx.shadowBlur=0;
                if(cam.z>0.55&&r>3.5){
                    var fontSize=Math.max(8.5,Math.min(11.5,r*1.1));
                    ctx.font='500 '+fontSize+'px Inter';ctx.textAlign='center';ctx.textBaseline='top';
                    ctx.fillStyle=hexToRGBA('#060710',alpha2*0.7);
                    var lbl=nd.name||'';if(lbl.length>18)lbl=lbl.substring(0,16)+'\u2026';
                    ctx.fillText(lbl,sp.x+0.5,sp.y+r+5.5);
                    ctx.fillStyle=hexToRGBA('#e0e4f0',alpha2*(isHov?0.92:0.6));
                    ctx.fillText(lbl,sp.x,sp.y+r+5)
                }
                ctx.globalAlpha=1
            })
        }

        function drawBipartiteLabels(){
            if(curProj!=='bipartite')return;
            ctx.save();ctx.font='600 9.5px "JetBrains Mono"';ctx.textAlign='center';ctx.letterSpacing='0.15em';
            ctx.fillStyle=hexToRGBA('#7BE0A0',0.4);ctx.fillText('PROCESS & CAPABILITY',W*0.22,50);
            ctx.fillStyle=hexToRGBA('#45B7D1',0.4);ctx.fillText('PRODUCT & INFRA',W*0.78,50);
            if(bipG.mid.length){ctx.fillStyle=hexToRGBA('#C9A44e',0.3);ctx.fillText('CONTEXT',W/2,50)}
            ctx.restore()
        }

        function drawUMAPInfo(){
            if(curProj!=='umap')return;
            ctx.save();ctx.font='400 9px "JetBrains Mono"';ctx.textAlign='left';
            ctx.fillStyle=hexToRGBA('#48e8d8',0.35);
            ctx.fillText('UMAP \u00B7 k='+umapK+' \u00B7 min_dist=0.1',16,H-38);
            ctx.restore()
        }

        function drawSpectralInfo(){
            if(curProj!=='spectral')return;
            ctx.save();ctx.font='400 9px "JetBrains Mono"';ctx.textAlign='left';
            ctx.fillStyle=hexToRGBA('#8B7BF0',0.35);ctx.fillText('Eigenvector 1 \u2192 X',16,H-38);ctx.fillText('Eigenvector 2 \u2192 Y',16,H-24);ctx.restore()
        }

        function drawChord(){
            if(curProj!=='chord')return;
            var vis=nodes.filter(function(n){return n.visible});var cats=Object.keys(cNC);if(cats.length<2)return;
            var cx=W/2,cy=H/2,R=Math.min(W,H)*0.36;var total=vis.length;var gap=0.03;
            var catArcs=[];var startA=-Math.PI/2;
            cats.forEach(function(c){var cnt=cNC[c]||0;var arc=2*Math.PI*(cnt/total)-gap;catArcs.push({cat:c,start:startA,end:startA+arc,cnt:cnt,color:CC[c]});startA+=arc+gap});
            var nodeArcs={};var ai={};catArcs.forEach(function(ca){ai[ca.cat]=0});
            vis.forEach(function(nd){var ca=catArcs.find(function(a){return a.cat===nd.category});if(!ca)return;var idx2=ai[nd.category]++;var slice=ca.end-ca.start;var na=slice/ca.cnt;var s=ca.start+idx2*na,e=s+na*0.9;nodeArcs[nd.id]={start:s,end:e,cat:nd.category}});
            ctx.lineCap='round';
            gE.forEach(function(e){if(!e.visible)return;var sa=nodeArcs[e.source],ta=nodeArcs[e.target];if(!sa||!ta)return;
                var x1=cx+Math.cos(sa.start)*R,y1=cy+Math.sin(sa.start)*R;var x2=cx+Math.cos(ta.start)*R,y2=cy+Math.sin(ta.start)*R;
                var isHov=chordHC&&(chordHC.source===e.source||chordHC.target===e.source||chordHC.source===e.target||chordHC.target===e.target);
                ctx.strokeStyle=hexToRGBA(FC[e.family]||'#48e8d8',isHov?0.28:0.04);ctx.lineWidth=isHov?1.5:0.6;
                ctx.beginPath();ctx.moveTo(x1,y1);ctx.quadraticCurveTo(cx,cy,x2,y2);ctx.stroke()
            });
            catArcs.forEach(function(ca){
                ctx.beginPath();ctx.arc(cx,cy,R-1,ca.start,ca.end);ctx.strokeStyle=hexToRGBA(ca.color,0.06);ctx.lineWidth=6;ctx.stroke();
                ctx.beginPath();ctx.arc(cx,cy,R,ca.start,ca.end);ctx.strokeStyle=hexToRGBA(ca.color,0.3);ctx.lineWidth=2.5;ctx.stroke();
                var ma=(ca.start+ca.end)/2;var lx=cx+Math.cos(ma)*(R+20),ly=cy+Math.sin(ma)*(R+20);
                ctx.font='500 8.5px "JetBrains Mono"';ctx.textAlign=Math.cos(ma)>0?'left':'right';ctx.textBaseline='middle';
                ctx.fillStyle=hexToRGBA(ca.color,0.55);ctx.fillText(shortLabel(ca.cat),lx,ly)
            });
            if(chordHC){var sa=nodeArcs[chordHC.source]||nodeArcs[chordHC.target];
                if(sa){ctx.beginPath();ctx.arc(cx,cy,R,sa.start,sa.end);ctx.strokeStyle=hexToRGBA('#ffffff',0.35);ctx.lineWidth=4;ctx.stroke()}}
            ctx.lineCap='butt'
        }

        function drawMinimap(){
            var mw=180,mh=125;mmC.width=mw*devicePixelRatio;mmC.height=mh*devicePixelRatio;
            mmX.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);mmX.clearRect(0,0,mw,mh);
            var vis=nodes.filter(function(n){return n.visible});if(!vis.length)return;
            var x1=Infinity,x2=-Infinity,y1=Infinity,y2=-Infinity;
            vis.forEach(function(n){if(n.x<x1)x1=n.x;if(n.x>x2)x2=n.x;if(n.y<y1)y1=n.y;if(n.y>y2)y2=n.y});
            if(x1===Infinity)return;var p=10,gw=x2-x1+p*2,gh=y2-y1+p*2,s=Math.min(mw/gw,mh/gh);
            var ox=mw/2-((x1+x2)/2)*s,oy=mh/2-((y1+y2)/2)*s;
            var mGrd=mmX.createRadialGradient(mw/2,mh/2,0,mw/2,mh/2,mw/2);
            mGrd.addColorStop(0,'rgba(12,13,22,0)');mGrd.addColorStop(1,'rgba(6,7,16,0.4)');
            mmX.fillStyle=mGrd;mmX.fillRect(0,0,mw,mh);
            vis.forEach(function(n){var mx=n.x*s+ox,my=n.y*s+oy;mmX.fillStyle=hexToRGBA(CC[n.category]||'#888',0.55);mmX.fillRect(mx-1,my-1,2,2)});
            var vx1=-cam.x/cam.z,vy1=-cam.y/cam.z;var vx2=(W-cam.x)/cam.z,vy2=(H-cam.y)/cam.z;
            var rx=vx1*s+ox,ry=vy1*s+oy,rw=(vx2-vx1)*s,rh=(vy2-vy1)*s;
            mmX.strokeStyle=hexToRGBA('#48e8d8',0.3);mmX.lineWidth=1;mmX.strokeRect(rx,ry,rw,rh)
        }

        /* ═══════ MAIN LOOP ═══════ */
        function render(){
            requestAnimationFrame(render);fc++;var now=performance.now();
            if(now-lt>=1000){fps=fc;fc=0;lt=now;document.getElementById('fps-counter').textContent=fps+' FPS'}
            uCP();simTick();interpTick();
            catC={};nodes.forEach(function(n){if(n.visible){if(!catC[n.category])catC[n.category]=[];catC[n.category].push(n)}});
            ctx.clearRect(0,0,W,H);drawAmbBlobs();drawDust();
            if(curProj==='chord'){drawChord()}
            else{drawHulls();drawEdges();drawNodes();drawBipartiteLabels();drawUMAPInfo();drawSpectralInfo()}
            drawToast();drawMinimap()
        }

        /* ═══════ HIT TESTING ═══════ */
        function hitNode(sx,sy){
            var wp=s2w(sx,sy);var best=null,bestD=Infinity;
            nodes.forEach(function(n){if(!n.visible)return;var dx=n.x-wp.x,dy=n.y-wp.y,d2=dx*dx+dy*dy;var r=(4.5+n.degree*0.55)*1.8;if(d2<r*r&&d2<bestD){bestD=d2;best=n}});
            return best
        }
        function hitChord(sx,sy){
            if(curProj!=='chord')return null;
            var cx2=W/2,cy2=H/2,R=Math.min(W,H)*0.36;
            var dx=sx-cx2,dy=sy-cy2,d=Math.sqrt(dx*dx+dy*dy);
            if(Math.abs(d-R)>15)return null;var ang=Math.atan2(dy,dx);
            var vis=nodes.filter(function(n){return n.visible});var cats=Object.keys(cNC);var total=vis.length;var gap=0.03;var startA=-Math.PI/2;
            for(var ci=0;ci<cats.length;ci++){var cnt=cNC[cats[ci]]||0;var arc=2*Math.PI*(cnt/total)-gap;
                if(ang>=startA&&ang<=startA+arc){var idx2=Math.floor((ang-startA)/arc*cnt);idx2=clamp(idx2,0,cnt-1);var catNodes=vis.filter(function(n){return n.category===cats[ci]});return catNodes[idx2]||null}
                startA+=arc+gap
            }
            return null
        }

        /* ═══════ TOOLTIP ═══════ */
        function showTT(nd,sx,sy){
            var tt=document.getElementById('tooltip');
            document.getElementById('tt-cat').textContent=shortLabel(nd.category);
            document.getElementById('tt-cat').style.color=CC[nd.category]||'#888';
            document.getElementById('tt-layer').textContent=nd.layer||'';
            document.getElementById('tt-layer').style.color=LC[nd.layer]||'#888';
            document.getElementById('tt-title').textContent=nd.name;
            document.getElementById('tt-desc').textContent=nd.description||'';
            document.getElementById('tt-year').textContent=nd.year?'c. '+nd.year:'';
            document.getElementById('tt-meta').innerHTML='<span>Conf. '+((nd.confidence||0)*100).toFixed(0)+'%</span><span>Deg. '+nd.degree+'</span><span>'+(nd.layer||'')+'</span>';
            tt.style.display='block';
            var tx=sx+16,ty=sy-10;
            if(tx+280>W)tx=sx-280;if(ty+170>H)ty=H-180;if(ty<10)ty=10;
            tt.style.left=tx+'px';tt.style.top=ty+'px'
        }
        function hideTT(){document.getElementById('tooltip').style.display='none'}

        /* ═══════ INSPECT PANEL ═══════ */
        function openInspect(nd){
            selN=nd;var raw=nd._raw||{};
            var panel=document.getElementById('inspect-panel');
            document.getElementById('ip-accent-bar').style.background='linear-gradient(90deg,'+(CC[nd.category]||'#888')+',transparent)';
            var badge=document.getElementById('ip-badge');
            badge.style.borderColor=hexToRGBA(CC[nd.category],0.35);badge.style.background=hexToRGBA(CC[nd.category],0.06);badge.style.color=CC[nd.category];
            document.getElementById('ip-badge-dot').style.background=CC[nd.category];
            document.getElementById('ip-badge-text').textContent=shortLabel(nd.category);
            var lb=document.getElementById('ip-layer-badge');
            lb.style.borderColor=hexToRGBA(LC[nd.layer]||'#888',0.25);lb.style.background=hexToRGBA(LC[nd.layer]||'#888',0.05);lb.style.color=LC[nd.layer]||'#888';
            document.getElementById('ip-layer-dot').style.background=LC[nd.layer]||'#888';
            document.getElementById('ip-layer-text').textContent=nd.layer||'Unknown';
            document.getElementById('ip-title').textContent=nd.name;
            document.getElementById('ip-desc').textContent=nd.description||'No description available.';

            /* Stats grid: confidence, degree, inheritance, earliest year */
            var earliestYear=nd.year||'\u2014';
            var sg=document.getElementById('ip-stats-grid');
            sg.innerHTML='<div class="ip-stat"><div class="ip-stat-value" style="color:'+confidenceColor(nd.confidence)+'">'+((nd.confidence||0)*100).toFixed(0)+'%</div><div class="ip-stat-label">Confidence</div></div>'
                +'<div class="ip-stat"><div class="ip-stat-value">'+nd.degree+'</div><div class="ip-stat-label">Degree</div></div>'
                +'<div class="ip-stat"><div class="ip-stat-value">'+(nd.inheritanceLevel||0)+'</div><div class="ip-stat-label">Inheritance</div></div>'
                +'<div class="ip-stat"><div class="ip-stat-value">'+earliestYear+'</div><div class="ip-stat-label">Earliest</div></div>';

            var dyn=document.getElementById('ip-dynamic-sections');dyn.innerHTML='';var secIdx=0;

            /* ── Domain Scope ── */
            var domains=raw.domainScope||[];
            if(domains.length){
                dyn.innerHTML+=secHtml(secIdx++,'Domain Scope','<div class="ip-array-tags">'+domains.map(function(d){return'<span class="ip-array-tag">'+escHTML(d)+'</span>'}).join('')+'</div>');
            }

            /* ── Functional Roles ── */
            var roles=raw.functionalRoles||[];
            if(roles.length){
                dyn.innerHTML+=secHtml(secIdx++,'Functional Roles','<div class="ip-array-tags">'+roles.map(function(r){return'<span class="ip-array-tag">'+escHTML(r)+'</span>'}).join('')+'</div>');
            }

            /* ── Category-Specific Fields ── */
            var specHtml=buildSpecificSection(raw);
            if(specHtml)dyn.innerHTML+=secHtml(secIdx++,'Category Details',specHtml);

            /* ── Relationships ── */
            var rels=raw.relationships||[];
            if(rels.length){
                var h='<ul class="ip-edge-list">';
                rels.forEach(function(rel){
                    var fam=rel.relationshipFamily||TFM[rel.relationshipType]||'';
                    var famC2=FC[fam]||FC['unknown']||'#48e8d8';
                    var tgtId=(rel.targetNodeId||'').replace(/\s+/g,'_');
                    var tgtNd=nM[tgtId];
                    var tgt=tgtNd?tgtNd.name:(rel.targetNodeId||'Unknown');
                    var famLabel=FLB[fam]||friendlyLabel(fam)||'Related';
                    var typeLabel=rel.relationshipType.replace(/_/g,' ');
                    h+='<li class="ip-edge-item"><div class="ip-edge-connector"><div class="ip-edge-dot" style="background:'+famC2+'"></div></div><div class="ip-edge-content"><span class="ip-edge-type" style="background:'+hexToRGBA(famC2,0.1)+';color:'+famC2+'">'+escHTML(famLabel)+'</span><span class="ip-edge-target">'+escHTML(tgt)+'</span>'+(rel.description?'<span class="ip-edge-desc">'+escHTML(rel.description)+'</span>':'')+'</div></li>'
                });
                h+='</ul>';dyn.innerHTML+=secHtml(secIdx++,'Relationships',h);
            }

            /* ── Historical Context (chronology) ── */
            var hc=raw.historicalContext;
            if(hc){
                var hcHtml='';
                if(hc.summary){hcHtml+='<div class="ip-hist-summary">'+escHTML(hc.summary)+'</div>'}
                if(hc.chronology&&hc.chronology.length){
                    hc.chronology.forEach(function(c){
                        hcHtml+='<div class="ip-chron-item"><div class="ip-chron-year">'+(isFiniteNum(c.year)?c.year:'?')+'</div><div class="ip-chron-event">'+escHTML(c.event)+'</div>'+(c.context?'<div class="ip-chron-ctx">'+escHTML(c.context)+'</div>':'')+'</div>'
                    })
                }
                if(hcHtml)dyn.innerHTML+=secHtml(secIdx++,'Historical Context',hcHtml);
            }

            /* ── Long Description ── */
            if(raw.longDescription){
                var ld=raw.longDescription;var preview=ld.substring(0,200);
                var ldbl='<div class="ip-long-desc-preview">'+escHTML(preview)+(ld.length>200?'\u2026':'')+'</div>'
                    +(ld.length>200?'<button class="ip-long-desc-toggle" onclick="this.classList.toggle(\'expanded\');this.nextElementSibling.classList.toggle(\'expanded\')"><span>Read more</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="ip-long-desc-content"><div class="ip-long-desc-text">'+escHTML(ld)+'</div></div>':'');
                dyn.innerHTML+='<div class="ip-long-desc-block" style="animation-delay:'+(secIdx++*0.05)+'s">'+ldbl+'</div>';
            }

            /* ── References ── */
            var refs=raw.references||[];
            if(refs.length){
                var rh='<div class="ip-ref-list">';
                refs.forEach(function(ref,i){
                    var title=ref.title||'Untitled';var desc=ref.description||'';var url=ref.link||'#';
                    var domain='';try{domain=new URL(url).hostname.replace(/^www\./,'')}catch(e){domain=url}
                    rh+='<a class="ip-ref-card" href="'+escHTML(url)+'" target="_blank" rel="noopener noreferrer" style="animation-delay:'+(i*0.04)+'s">'
                        +'<div class="ip-ref-header"><div class="ip-ref-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></div>'
                        +'<div class="ip-ref-titles"><span class="ip-ref-title">'+escHTML(title)+'</span><span class="ip-ref-domain">'+escHTML(domain)+'</span></div>'
                        +'<svg class="ip-ref-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg></div>'
                        +(desc?'<div class="ip-ref-desc">'+escHTML(desc)+'</div>':'')+'</a>'
                });
                rh+='</div>';dyn.innerHTML+=secHtml(secIdx++,'References',rh);
            }

            /* ── Metadata ── */
            var meta=raw.metadata||{};
            var metaHtml='';
            if(meta.sourceReference)metaHtml+='<div class="ip-meta-row"><span class="ip-meta-key">Source</span><span class="ip-meta-val">'+escHTML(meta.sourceReference)+'</span></div>';
            if(meta.createdAt)metaHtml+='<div class="ip-meta-row"><span class="ip-meta-key">Created</span><span class="ip-meta-val">'+escHTML(meta.createdAt)+'</span></div>';
            var tags=meta.tags||[];
            if(tags.length)metaHtml+='<div style="margin-top:8px" class="ip-tags">'+tags.map(function(t){return'<span class="ip-tag">'+escHTML(t)+'</span>'}).join('')+'</div>';
            if(meta.auditTrail&&meta.auditTrail.length){
                metaHtml+='<div style="margin-top:10px">';
                meta.auditTrail.forEach(function(a){
                    metaHtml+='<div class="ip-audit-item"><div class="ip-audit-date">'+escHTML(a.reviewDate||'')+'</div><div class="ip-audit-note">'+escHTML(a.reviewNote||'')+'</div></div>'
                });
                metaHtml+='</div>'
            }
            if(metaHtml)dyn.innerHTML+=secHtml(secIdx++,'Metadata',metaHtml);

            panel.classList.add('open')
        }

        /* Helper: build a section div */
        function secHtml(idx,title,content){
            return'<div class="ip-section" style="animation-delay:'+(idx*0.05)+'s"><div class="ip-section-title">'+escHTML(title)+'</div>'+content+'</div>'
        }

        /* Helper: build category-specific section from schema's `specific` field */
        function buildSpecificSection(raw){
            var spec=raw.specific;if(!spec)return'';
            var cat=raw.category;var html='';
            if(cat==='Product'){
                html+=propRow('Materiality',spec.materiality);
                html+=propRow('Use Case',spec.useCase);
                html+=propRow('Lifecycle',spec.lifeCycleStage,'enum');
            }else if(cat==='ProductionProcess'){
                if(spec.inputs&&spec.inputs.length)html+='<div style="margin-bottom:6px"><span class="ip-prop-key" style="display:inline-block;margin-bottom:4px">Inputs</span><div class="ip-array-tags">'+spec.inputs.map(function(x){return'<span class="ip-array-tag">'+escHTML(x)+'</span>'}).join('')+'</div></div>';
                if(spec.outputs&&spec.outputs.length)html+='<div style="margin-bottom:6px"><span class="ip-prop-key" style="display:inline-block;margin-bottom:4px">Outputs</span><div class="ip-array-tags">'+spec.outputs.map(function(x){return'<span class="ip-array-tag">'+escHTML(x)+'</span>'}).join('')+'</div></div>';
                html+=propRow('Transform Logic',spec.transformationLogic);
            }else if(cat==='Technique'){
                html+=propRow('Knowledge Type',spec.knowledgeType);
                html+=propRow('Codification',spec.codificationLevel,'enum');
                html+=propRow('Transfer',spec.transferMechanism);
            }else if(cat==='Capability'){
                html+=propRow('Type',spec.capabilityType);
                html+=propRow('Proficiency',spec.proficiencyLevel);
                html+=propRow('Measurability',spec.measurability);
            }else{
                /* Generic: show all key-value pairs */
                for(var k in spec){if(spec.hasOwnProperty(k))html+=propRow(k,spec[k])}
            }
            return html?'<div class="ip-prop-list">'+html+'</div>':''
        }

        function propRow(key,val,type){
            if(val===undefined||val===null)return'';
            var display=val;
            if(type==='enum'){display='<span class="ip-enum-badge" style="border-color:rgba(72,232,216,0.2);color:rgba(72,232,216,0.7);background:rgba(72,232,216,0.04)">'+escHTML(val)+'</span>'}
            else if(typeof val==='string'&&val.length>60)display='<span style="word-break:break-word">'+escHTML(val)+'</span>';
            else display=escHTML(String(val));
            return'<div class="ip-prop-row"><span class="ip-prop-key">'+escHTML(friendlyLabel(key))+'</span><span class="ip-prop-val">'+display+'</span></div>'
        }

        function closeInspect(){document.getElementById('inspect-panel').classList.remove('open');selN=null}

        /* ═══════ SEARCH ═══════ */
        function posDropdown(){
            var dd=document.getElementById('search-dropdown');var inp=document.getElementById('search-input');var r=inp.getBoundingClientRect();
            dd.style.top=(r.bottom+4)+'px';dd.style.left=r.left+'px';dd.style.width=Math.max(300,r.width)+'px'
        }

        function doSearch(q){
            var dd=document.getElementById('search-dropdown');var inner=document.getElementById('search-dropdown-inner');posDropdown();
            if(!q){dd.classList.remove('open');ddOpen=false;fRes=[];return}
            fRes=nodes.filter(function(n){
                var nm=(n.name||'').toLowerCase();var sl=shortLabel(n.category).toLowerCase();
                var dl=(n.description||'').toLowerCase();var ly=(n.layer||'').toLowerCase();
                var doms=(n._raw&&n._raw.domainScope||[]).join(' ').toLowerCase();
                return nm.indexOf(q.toLowerCase())>=0||sl.indexOf(q.toLowerCase())>=0||dl.indexOf(q.toLowerCase())>=0||n.category.toLowerCase().indexOf(q.toLowerCase())>=0||ly.indexOf(q.toLowerCase())>=0||doms.indexOf(q.toLowerCase())>=0
            }).slice(0,20);
            if(!fRes.length){inner.innerHTML='<div class="search-empty-hint">No matching nodes</div>';dd.classList.add('open');ddOpen=true;document.getElementById('search-dropdown-count').textContent='0';return}
            document.getElementById('search-dropdown-count').textContent=fRes.length;
            var html='';fRes.forEach(function(nd,i){
                var isAct=selN&&selN.id===nd.id;
                html+='<div class="search-result'+(isAct?' active':'')+'" data-idx="'+i+'"><div class="sr-cat-line" style="background:'+(CC[nd.category]||'#888')+'"></div><div class="sr-body"><div class="sr-top"><span class="sr-name">'+hlMatch(nd.name,q)+'</span><span class="sr-cat-label" style="color:'+(CC[nd.category]||'#888')+'">'+(nd.layer||'')+'</span></div><div class="sr-desc">'+(nd.description||'')+'</div><div class="sr-foot"><span>Conf. '+((nd.confidence||0)*100).toFixed(0)+'%</span><span>Deg. '+nd.degree+'</span>'+(nd.year?'<span>c. '+nd.year+'</span>':'')+'</div></div></div>'
            });
            inner.innerHTML=html;
            inner.querySelectorAll('.search-result').forEach(function(el){
                el.addEventListener('click',function(){selectSearchResult(parseInt(el.dataset.idx))});
                el.addEventListener('mouseenter',function(){kbFI=parseInt(el.dataset.idx);uKBF()})
            });
            dd.classList.add('open');ddOpen=true;kbFI=0;uKBF()
        }

        function uKBF(){var items=document.getElementById('search-dropdown-inner').querySelectorAll('.search-result');items.forEach(function(el,i){el.classList.toggle('kb-focus',i===kbFI)})}
        function selectSearchResult(idx){
            var nd=fRes[idx];if(!nd)return;pinN=nd;
            document.getElementById('search-selected').classList.add('visible');
            document.getElementById('search-selected-dot').style.background=CC[nd.category];
            document.getElementById('search-selected-name').textContent=nd.name;
            document.getElementById('search-dropdown').classList.remove('open');ddOpen=false;
            document.getElementById('search-input').value='';document.getElementById('search-clear').classList.remove('visible');
            pTN(nd);triggerToast(nd);openInspect(nd)
        }
        function clearSearchSel(){pinN=null;document.getElementById('search-selected').classList.remove('visible')}

        /* ═══════ EVENT HANDLERS ═══════ */
        canvas.addEventListener('mousedown',function(e){
            var r=canvas.getBoundingClientRect();var sx=e.clientX-r.left,sy=e.clientY-r.top;
            if(curProj==='chord'){var nd=hitChord(sx,sy);if(nd){openInspect(nd);pTN(nd)}return}
            var nd=hitNode(sx,sy);
            if(nd){dragN=nd;canvas.classList.add('locked')}else{isPan=true;panS={x:e.clientX-cam.x,y:e.clientY-cam.y};canvas.classList.add('locked')}
        });
        canvas.addEventListener('mousemove',function(e){
            var r=canvas.getBoundingClientRect();var sx=e.clientX-r.left,sy=e.clientY-r.top;
            mS={x:e.clientX,y:e.clientY};wM={x:sx,y:sy};
            if(dragN){var wp=s2w(sx,sy);dragN.x=wp.x;dragN.y=wp.y;dragN.vx=0;dragN.vy=0;if(SP.indexOf(curProj)>=0){dragN.targetX=wp.x;dragN.targetY=wp.y}return}
            if(isPan){cam.x=e.clientX-panS.x;cam.y=e.clientY-panS.y;camTgt=null;return}
            if(curProj==='chord'){var nd=hitChord(sx,sy);if(nd){chordHC=nd;showTT(nd,sx,sy)}else{chordHC=null;hideTT()}return}
            var nd=hitNode(sx,sy);
            if(nd!==hovN){hovN=nd;if(nd)showTT(nd,sx,sy);else hideTT()}else if(nd)showTT(nd,sx,sy)
        });
        canvas.addEventListener('mouseup',function(e){
            var r=canvas.getBoundingClientRect();var sx=e.clientX-r.left,sy=e.clientY-r.top;
            if(dragN&&!isPan){var wp0=s2w(sx,sy),dx=dragN.x-wp0.x,dy=dragN.y-wp0.y;if(Math.sqrt(dx*dx+dy*dy)<3)openInspect(dragN)}
            dragN=null;isPan=false;canvas.classList.remove('locked')
        });
        canvas.addEventListener('mouseleave',function(){hovN=null;chordHC=null;hideTT();if(!dragN){isPan=false;canvas.classList.remove('locked')}});
        canvas.addEventListener('wheel',function(e){
            e.preventDefault();var r=canvas.getBoundingClientRect();var sx=e.clientX-r.left,sy=e.clientY-r.top;
            var wp=s2w(sx,sy);var f=e.deltaY>0?0.9:1.1;var nz=clamp(cam.z*f,0.05,8);
            cam.x=sx-wp.x*nz;cam.y=sy-wp.y*nz;cam.z=nz;camTgt=null
        },{passive:false});

        document.getElementById('minimap-wrap').addEventListener('click',function(e){
            var r=this.getBoundingClientRect();var sx=e.clientX-r.left,sy=e.clientY-r.top;
            var vis=nodes.filter(function(n){return n.visible});if(!vis.length)return;
            var x1=Infinity,x2=-Infinity,y1=Infinity,y2=-Infinity;
            vis.forEach(function(n){if(n.x<x1)x1=n.x;if(n.x>x2)x2=n.x;if(n.y<y1)y1=n.y;if(n.y>y2)y2=n.y});
            if(x1===Infinity)return;var p=10,gw=x2-x1+p*2,gh=y2-y1+p*2,s=Math.min(180/gw,125/gh);
            var ox=90-((x1+x2)/2)*s,oy=62.5-((y1+y2)/2)*s;
            var wx=(sx-ox)/s,wy=(sy-oy)/s;cam.x=W/2-wx*cam.z;cam.y=H/2-wy*cam.z;camTgt=null
        });

        document.addEventListener('keydown',function(e){
            if(e.key==='Escape'){closeInspect();clearSearchSel();document.getElementById('search-dropdown').classList.remove('open');ddOpen=false;document.getElementById('search-input').blur();toastNode=null}
            if(e.key==='f'&&!e.ctrlKey&&!e.metaKey&&document.activeElement.tagName!=='INPUT'){e.preventDefault();fCam()}
            if(ddOpen){
                if(e.key==='ArrowDown'){e.preventDefault();kbFI=Math.min(kbFI+1,fRes.length-1);uKBF();var el=document.querySelector('.search-result.kb-focus');if(el)el.scrollIntoView({block:'nearest'})}
                if(e.key==='ArrowUp'){e.preventDefault();kbFI=Math.max(kbFI-1,0);uKBF();var el2=document.querySelector('.search-result.kb-focus');if(el2)el2.scrollIntoView({block:'nearest'})}
                if(e.key==='Enter'){e.preventDefault();if(kbFI>=0&&kbFI<fRes.length)selectSearchResult(kbFI)}
            }
        });

        document.getElementById('sidebar-toggle-btn').addEventListener('click',function(){document.body.classList.toggle('sidebar-collapsed');setTimeout(resize,550)});
        document.getElementById('qa-fit').addEventListener('click',function(){fCam()});
        document.getElementById('ip-close-btn').addEventListener('click',closeInspect);

        document.getElementById('search-input').addEventListener('input',function(){var q=this.value.trim();document.getElementById('search-clear').classList.toggle('visible',q.length>0);doSearch(q)});
        document.getElementById('search-input').addEventListener('focus',function(){if(this.value.trim())doSearch(this.value.trim())});
        document.getElementById('search-clear').addEventListener('click',function(){document.getElementById('search-input').value='';this.classList.remove('visible');doSearch('')});
        document.getElementById('search-selected-clear').addEventListener('click',clearSearchSel);

        document.getElementById('projection-chips').addEventListener('click',function(e){
            var chip=e.target.closest('.proj-chip');if(!chip)return;var pj=chip.dataset.proj;if(pj===curProj)return;
            this.querySelectorAll('.proj-chip').forEach(function(c){c.classList.remove('active')});chip.classList.add('active');uPS();
            if(curProj!=='chord'){sPC(curProj);wasChord=false}else{wasChord=true}
            curProj=pj;document.getElementById('hud-proj').textContent=PL[pj]||pj;
            var infoEl=document.getElementById('hud-proj-info');
            if(pj==='umap')infoEl.textContent='k='+umapK+' \u00B7 min_dist=0.1';
            else if(pj==='spectral')infoEl.textContent='Laplacian eigenvectors';
            else if(pj==='bipartite')infoEl.textContent='Process \u27F7 Product';
            else infoEl.textContent='';
            toastNode=null;
            if(pj==='chord'){cam={x:0,y:0,z:1};camTgt=null}
            else{if(SP.indexOf(pj)>=0){applyProjection(pj);fCam()}else if(!wasChord&&rPC(pj)){fCam()}else{reheatAlpha();fCam()}}
        });

        document.querySelectorAll('#lens-controls .toggle-item').forEach(function(el){
            var conflicts=(el.dataset.conflict||'').split(',');
            el.querySelector('input').addEventListener('change',function(){
                if(this.checked){var self=this;conflicts.forEach(function(c){if(c===curProj){self.checked=false;return}var other=document.querySelector('#lens-'+c);if(other&&other.checked&&other!==self){other.checked=false}})}
            })
        });

        document.getElementById('reset-all-btn').addEventListener('click',function(){
            aCats=new Set(CL);aFams=new Set(FL);aLayers=new Set(LL);
            tR={min:tRF.min,max:tRF.max};document.getElementById('time-min').value=0;document.getElementById('time-max').value=1000;
            uTimeFill();uFilt();buildCatToggles();buildFamilyChips();rLC();
            document.getElementById('lens-hulls').checked=true;document.getElementById('lens-heatmap').checked=false;
            document.getElementById('lens-centrality').checked=false;document.getElementById('lens-confidence-color').checked=false;
            document.getElementById('lens-flow').checked=true;document.getElementById('lens-observability').checked=false;
            clearSearchSel();closeInspect();toastNode=null;curProj='default';wasChord=false;
            document.querySelectorAll('.proj-chip').forEach(function(c){c.classList.remove('active')});
            document.querySelector('.proj-chip[data-proj="default"]').classList.add('active');uPS();
            document.getElementById('hud-proj').textContent='Force';document.getElementById('hud-proj-info').textContent='';
            reheatAlpha();pCache={};cam={x:0,y:0,z:1};camTgt=null;fCam()
        });

        /* ═══════ TIME SLIDER ═══════ */
        function uTimeFill(){
            var mn=parseInt(document.getElementById('time-min').value);var mx=parseInt(document.getElementById('time-max').value);
            if(mn>mx){var tmp=mn;mn=mx;mx=tmp}
            var range=tRF.max-tRF.min;if(range<=0)range=1;
            tR.min=tRF.min+mn/1000*range;tR.max=tRF.min+mx/1000*range;
            var fill=document.getElementById('time-fill');fill.style.left=(mn/10)+'%';fill.style.width=((mx-mn)/10)+'%';
            fill.classList.toggle('active',mn>0||mx<1000);
            document.getElementById('time-min-label').textContent=tR.min>0?'c. '+Math.round(tR.min):'\u2014';
            document.getElementById('time-max-label').textContent=tR.max<Infinity?'c. '+Math.round(tR.max):'\u2014'
        }
        document.getElementById('time-min').addEventListener('input',function(){uTimeFill();uFilt()});
        document.getElementById('time-max').addEventListener('input',function(){uTimeFill();uFilt()});

        /* ═══════ BUILD CATEGORY TOGGLES ═══════ */
        function buildCatToggles(){
            var html='';CL.forEach(function(c){
                html+='<label class="toggle-item" id="ctog-'+c+'" data-cat="'+c+'"><input type="checkbox" checked><span class="checkmark"></span><span class="cat-dot" style="background:'+CC[c]+'"></span><span>'+shortLabel(c)+'</span><span class="node-count">'+(cNC[c]||0)+'</span></label>'
            });
            document.getElementById('category-toggles').innerHTML=html;
            document.getElementById('category-toggles').querySelectorAll('.toggle-item').forEach(function(el){
                el.querySelector('input').addEventListener('change',function(){var cat=el.dataset.cat;if(this.checked)aCats.add(cat);else aCats.delete(cat);uFilt()})
            })
        }

        /* ═══════ BUILD FAMILY CHIPS ═══════ */
        function buildFamilyChips(){
            var html='';FL.forEach(function(f){
                var label=(FLB[f]||friendlyLabel(f));if(f==='unknown')label='Unspecified';
                var col=FC[f]||'#888';
                html+='<div class="chip active" data-family="'+f+'" style="border-left-color:'+col+'">'+label+'</div>'
            });
            document.getElementById('family-chips').innerHTML=html;
            document.getElementById('family-chips').querySelectorAll('.chip').forEach(function(el){
                el.addEventListener('click',function(){var f=el.dataset.family;if(el.classList.contains('active')){aFams.delete(f);el.classList.remove('active')}else{aFams.add(f);el.classList.add('active')}uFilt()})
            })
        }

        /* ═══════ DATA INIT (Schema-Aligned) ═══════ */
        function initGraph(data){
            deriveSchema(data);nM={};nodes=[];gE=[];minY=Infinity;maxY=-Infinity;maxIL=1;var degC={};

            data.forEach(function(r){
                if(!r.id)return;
                var id=r.id.replace(/\s+/g,'_');
                /* Extract earliest year from historicalContext.chronology */
                var yr=null;
                if(r.historicalContext&&r.historicalContext.chronology){
                    var years=r.historicalContext.chronology.map(function(c){return c.year}).filter(isFiniteNum);
                    if(years.length)yr=Math.min.apply(null,years)
                }
                if(yr!==null&&yr<minY)minY=yr;if(yr!==null&&yr>maxY)maxY=yr;
                var il=r.inheritanceLevel||0;if(il>maxIL)maxIL=il;
                var initSpread=Math.max(800,Math.sqrt(data.length)*60);
                /* Derive layer from category since schema has no layer field */
                var layer=CLL[r.category]||'Strategic Space';
                var nd={
                    id:id,name:r.name||r.id,category:r.category,layer:layer,
                    description:r.description||'',
                    confidence:((r.metadata&&r.metadata.confidenceScore)||0.7),
                    degree:0,inheritanceLevel:il,
                    year:yr,
                    x:(Math.random()-.5)*initSpread,y:(Math.random()-.5)*initSpread,
                    vx:0,vy:0,visible:true,_raw:r
                };
                nodes.push(nd);nM[id]=nd;degC[id]=0
            });

            data.forEach(function(r){
                if(!r.relationships)return;
                r.relationships.forEach(function(rel){
                    var sid=r.id.replace(/\s+/g,'_');
                    var tid=(rel.targetNodeId||'').replace(/\s+/g,'_');
                    if(!nM[sid]||!nM[tid])return;
                    /* Use explicit family from data, fallback to type-based mapping */
                    var fam=rel.relationshipFamily||TFM[rel.relationshipType]||'unknown';
                    gE.push({source:sid,target:tid,family:fam,type:rel.relationshipType||'',visible:true,description:rel.description||''});
                    degC[sid]=(degC[sid]||0)+1;degC[tid]=(degC[tid]||0)+1
                })
            });

            nodes.forEach(function(n){n.degree=degC[n.id]||0});
            tRF.min=minY===Infinity?0:minY;tRF.max=maxY===-Infinity?2025:maxY;
            tR.min=tRF.min;tR.max=tRF.max;
            document.getElementById('time-total-count').textContent=nodes.length;
            buildCatToggles();buildFamilyChips();rLC();uTimeFill();uFilt();
            sCV();fCam();uPS();dLoaded=true;initAmbBlobs();initDust();
            document.getElementById('loading-overlay').classList.add('hidden')
        }

        /* ═══════ FETCH ═══════ */
        var loaderMsg=document.getElementById('loader-msg');
        loaderMsg.textContent='Loading product space';
        fetch('../data/product/dataset.json')
            .then(function(r){if(!r.ok)throw new Error('HTTP '+r.status);return r.json()})
            .then(function(d){
                loaderMsg.textContent='Building graph';
                var arr=Array.isArray(d)?d:(d.nodes||d.categories||[]);
                if(!arr.length)throw new Error('Empty dataset');
                setTimeout(function(){initGraph(arr)},60)
            })
            .catch(function(err){
                loaderMsg.innerHTML='<span class="loader-error">Failed to load product space data.<br><br>'+escHTML(err.message)+'<br><br>Ensure <code style="font-size:.65rem;opacity:.6">data/dataset.json</code> exists and conforms to the Product Space Node Schema.</span>'
            });

        /* ═══════ BOOT ═══════ */
        resize();render();window.addEventListener('resize',resize);
    </script>
</body>
</html>
```