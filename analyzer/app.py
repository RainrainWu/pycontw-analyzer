"""
analyzer.app is the entrypoint of whole program.
"""

from analyzer.inspector import sponsor, program
from analyzer.visualizer import sunburst, pie, bar

# Potential sponsors by the numbers of discoveries
sponsors = sponsor.filter_potential_sponsor_by_times()
bar.plot_dict(sponsors)

# Potential sponsors by the attendee above C-level
sponsors = sponsor.filter_potential_sponsor_by_level()
print(sponsors)

# Pie chart for proportions of each program topics
mapping = program.get_proportion_of_categories()
pie.plot_dict(mapping)

# Sunburst chart for program hierarchy
hier = program.get_number_of_categories_and_levels()
sunburst.plot_two_levels_dict(hier)
