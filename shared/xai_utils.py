def generate_explanation(feature_names, values, weights):
    explanation = []
    for f, v, w in zip(feature_names, values, weights):
        impact = "Increase Risk" if w > 0 else "Reduce Risk"
        explanation.append({
            "Feature": f,
            "Value": v,
            "Impact": impact
        })
    return explanation
