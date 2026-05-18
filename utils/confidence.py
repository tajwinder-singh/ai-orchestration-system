# Confidence is based on score separation between
# the top retrieval results. Small gaps usually
# indicate ambiguous retrieval.
def compute_confidence(scores):
    if not scores:
        return 0.0

    top_score = scores[0]

    if len(scores) > 1:
        confidence = top_score - scores[1]
    else:
        confidence = top_score

    return round(float(max(confidence, 0.0)), 2)