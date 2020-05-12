"""
analyzer.app is the entrypoint of whole program.
"""

from analyzer.inspector import sponsor

print("Potential sponsors by the numbers of discoveries\n" + "=" * 50)
sponsor.filter_potential_sponsor_by_times()
print("\n")

print("Potential sponsors by the attendee above C-level\n" + "=" * 50)
sponsor.filter_potential_sponsor_by_level()
print("\n")
