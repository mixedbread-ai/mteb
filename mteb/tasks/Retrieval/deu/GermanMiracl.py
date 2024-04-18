from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class GermanMiracl(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="De-Miracl",
        description="De-Miracl",
        reference=None,
        dataset={
            "path": "openbread/De-Miracl",
            "revision": "main",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["dev"],
        eval_langs=["deu-Latn"],
        main_score="ndcg_at_10",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation=None,
        n_samples=None,
        avg_character_length=None,
    )
