from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Run and show/save the categorical plot
cat_plot_fig = draw_cat_plot()
cat_plot_fig.savefig('catplot.png')

# Run and show/save the heat map
heat_map_fig = draw_heat_map()
heat_map_fig.savefig('heatmap.png')

# Optional: Run the tests
#import test_module
#test_module.test_draw_cat_plot()
#test_module.test_draw_heat_map()