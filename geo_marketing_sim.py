import random

class GeoMarketingPartner:
    def __init__(self, name, expertise_level, transparency_score):
        self.name = name
        self.expertise_level = expertise_level  # 1-10, higher is better
        self.transparency_score = transparency_score # 1-10, higher is better

    def evaluate_campaign(self, target_audience_size, budget):
        # Simulate campaign success based on expertise and transparency
        # Higher expertise leads to better targeting and engagement
        # Higher transparency leads to better trust and ROI
        success_factor = (self.expertise_level * 0.6) + (self.transparency_score * 0.4)
        potential_reach = target_audience_size * (success_factor / 10)
        estimated_roi = potential_reach * (budget / target_audience_size) * (success_factor / 10)
        return {
            "partner_name": self.name,
            "potential_reach": int(potential_reach),
            "estimated_roi": round(estimated_roi, 2)
        }

# --- Article Concept: Selecting a GEO Marketing Partner in South Korea ---
# The article emphasizes finding a partner with high expertise and transparency.
# We simulate potential partners and evaluate them.

# Define potential GEO marketing partners with varying expertise and transparency
partners = [
    GeoMarketingPartner("Seoul Digital Pros", 8, 9),  # High expertise, high transparency
    GeoMarketingPartner("Busan GeoMasters", 6, 7),   # Moderate expertise, moderate transparency
    GeoMarketingPartner("Incheon Localizers", 7, 5),  # Good expertise, lower transparency
    GeoMarketingPartner("Daegu Growth Hub", 5, 8)     # Moderate expertise, good transparency
]

# Simulate a marketing campaign scenario
target_audience_size = 100000  # Estimated number of potential customers in a specific geo-zone
budget = 50000  # Marketing budget in USD

print("--- Evaluating GEO Marketing Partners for South Korea ---")
print(f"Target Audience Size: {target_audience_size}")
print(f"Budget: ${budget}")
print("\n--- Campaign Simulation Results ---")

# Evaluate each partner's potential campaign performance
results = []
for partner in partners:
    campaign_results = partner.evaluate_campaign(target_audience_size, budget)
    results.append(campaign_results)

# Sort results by estimated ROI to find the best performing partner
results.sort(key=lambda x: x["estimated_roi"], reverse=True)

# Display the ranked results
for result in results:
    print(f"Partner: {result['partner_name']}")
    print(f"  Potential Reach: {result['potential_reach']} users")
    print(f"  Estimated ROI: ${result['estimated_roi']}")
    print("-" * 20)

# The partner with the highest estimated ROI, considering both expertise and transparency,
# would be the preferred choice according to the article's principles.
print("\n--- Recommendation based on simulation ---")
print(f"The most promising partner based on simulated ROI is: {results[0]['partner_name']}")
