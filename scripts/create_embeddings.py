import json
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import SKOS
from sentence_transformers import SentenceTransformer

def create_embedding_text(graph, concept):
    """Creates a descriptive text for a SKOS concept."""
    parts = []
    
    pref_label = graph.value(concept, SKOS.prefLabel)
    if pref_label:
        parts.append(str(pref_label))

    broader = graph.value(concept, SKOS.broader)
    if broader:
        broader_label = graph.value(broader, SKOS.prefLabel)
        if broader_label:
            parts.append(f"vom Typ {broader_label},")

    alt_labels = [str(label) for label in graph.objects(concept, SKOS.altLabel)]
    if alt_labels:
        parts.append(f"auch bekannt als{', '.join(alt_labels)},")

    definition = graph.value(concept, SKOS.definition)
    if definition:
        parts.append(f"definiert als {definition},")
        
    scope_note = graph.value(concept, SKOS.scopeNote)
    if scope_note:
        parts.append(f"folgendermaßen verwendet: {scope_note}")

    return ", ".join(parts)

def main():
    """Main function to generate and save embeddings."""
    g = Graph()
    g.parse("C:\\repos\\WaiRKBLAETTER\\public\\thesaurus\\thesaurus.ttl", format="turtle")

    model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

    embeddings = {}
    for concept in g.subjects(predicate=URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), object=SKOS.Concept):
        text = create_embedding_text(g, concept)
        if text:
            embedding = model.encode(text, convert_to_tensor=False).tolist()
            embeddings[str(concept)] = embedding

    with open("C:\\repos\\WaiRKBLAETTER\\public\\thesaurus\\thesaurus_embeddings.json", "w") as f:
        json.dump(embeddings, f)

if __name__ == "__main__":
    main()
