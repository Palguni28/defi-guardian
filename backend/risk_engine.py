def calculate_risk(top_holders_percent, liquidity_locked_days, ownership_renounced, token_age_days, audit_status):
    risk = 0

    # Top Holders (30)
    if top_holders_percent > 80:
        risk += 30
    elif top_holders_percent > 60:
        risk += 20
    elif top_holders_percent > 40:
        risk += 10
    else:
        risk += 5

    # Liquidity (20)
    if liquidity_locked_days == 0:
        risk += 20
    elif liquidity_locked_days < 30:
        risk += 15
    elif liquidity_locked_days < 90:
        risk += 10
    elif liquidity_locked_days < 180:
        risk += 5
    else:
        risk += 2

    # Ownership (20)
    if ownership_renounced == "no":
        risk += 20
    elif ownership_renounced == "partial":
        risk += 10
    else:
        risk += 2

    # Token Age (15)
    if token_age_days < 7:
        risk += 15
    elif token_age_days < 30:
        risk += 10
    elif token_age_days < 90:
        risk += 5
    else:
        risk += 2

    # Audit (15)
    if audit_status == "none":
        risk += 15
    elif audit_status == "self-audited":
        risk += 8
    elif audit_status == "third-party-unverified":
        risk += 5
    else:
        risk += 2

        # Risk Label
    if risk > 75:
        label = "Very Risky"
    elif risk > 55:
        label = "Risky"
    elif risk > 35:
        label = "Moderate"
    elif risk > 13:
        label = "Low Risk"
    else:
        label = "Very Safe"

    return {"score": risk, "label": label}
