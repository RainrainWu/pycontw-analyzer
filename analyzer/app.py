"""
analyzer.app is the entrypoint of whole program.
"""

from analyzer.inspector import sponsor

sponsor.filter_potential_sponsor_by_times(3)
print('-'* 50)
sponsor.filter_potential_sponsor_by_level()
