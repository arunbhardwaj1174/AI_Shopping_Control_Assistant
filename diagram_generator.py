import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from datetime import datetime


class ArchitectureDiagramGenerator:
    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.docs_dir = self.root / "docs"
        self.docs_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_architecture_diagram(self):
        """Generate architecture layer diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Title
        ax.text(5, 9.5, 'AI Shopping Control Assistant - Architecture', 
                fontsize=16, weight='bold', ha='center')
        
        # Layer boxes with colors
        layers = [
            {'name': 'GUI Layer', 'y': 7.5, 'color': '#E8F4F8', 
             'components': ['main_window.py', 'input_frame.py', 'result_frame.py', 'dashboard.py']},
            {'name': 'ML Layer', 'y': 5.5, 'color': '#FFF4E6',
             'components': ['predictor.py', 'decision_rules.py', 'regret_classifier.py']},
            {'name': 'Database Layer', 'y': 3.5, 'color': '#F0F8FF',
             'components': ['db.py', 'purchase_history.db']},
            {'name': 'Utility Layer', 'y': 1.5, 'color': '#F0FFF0',
             'components': ['validation.py', 'charts.py', 'file_handler.py', 'data_loader.py']},
        ]
        
        for layer in layers:
            # Draw box
            box = mpatches.FancyBboxPatch((0.5, layer['y']-0.4), 9, 1.2,
                                         boxstyle="round,pad=0.1", 
                                         facecolor=layer['color'],
                                         edgecolor='black', linewidth=2)
            ax.add_patch(box)
            
            # Layer name
            ax.text(1, layer['y']+0.3, layer['name'], 
                   fontsize=12, weight='bold')
            
            # Components
            components_text = ' | '.join(layer['components'])
            ax.text(1.5, layer['y']-0.1, components_text,
                   fontsize=9, style='italic')
        
        # Add data flow arrows
        for i in range(len(layers)-1):
            ax.arrow(5, layers[i]['y']-0.5, 0, -0.4, 
                    head_width=0.3, head_length=0.1, fc='gray', ec='gray')
        
        # Save figure
        filepath = self.docs_dir / "architecture_diagram.png"
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return {"status": "success", "path": str(filepath)}
    
    def generate_flowchart(self):
        """Generate prediction flow diagram"""
        fig, ax = plt.subplots(figsize=(10, 12))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 14)
        ax.axis('off')
        
        # Title
        ax.text(5, 13.5, 'Prediction Flow', 
                fontsize=16, weight='bold', ha='center')
        
        # Define flowchart steps
        steps = [
            {'y': 12.5, 'text': 'Start', 'color': '#90EE90', 'shape': 'oval'},
            {'y': 11.5, 'text': 'User Input', 'color': '#87CEEB', 'shape': 'box'},
            {'y': 10.5, 'text': 'Validate Input', 'color': '#87CEEB', 'shape': 'box'},
            {'y': 9.3, 'text': 'Input Valid?', 'color': '#FFD700', 'shape': 'diamond'},
            {'y': 7.8, 'text': 'Load ML Model', 'color': '#FFA07A', 'shape': 'box'},
            {'y': 6.8, 'text': 'Generate Prediction', 'color': '#FFA07A', 'shape': 'box'},
            {'y': 5.8, 'text': 'Evaluate Decision Rules', 'color': '#DDA0DD', 'shape': 'box'},
            {'y': 4.8, 'text': 'Store in Database', 'color': '#B0C4DE', 'shape': 'box'},
            {'y': 3.8, 'text': 'Update Dashboard', 'color': '#87CEEB', 'shape': 'box'},
            {'y': 2.8, 'text': 'Display Result', 'color': '#87CEEB', 'shape': 'box'},
            {'y': 1.8, 'text': 'End', 'color': '#FFB6C1', 'shape': 'oval'},
        ]
        
        # Draw boxes
        for i, step in enumerate(steps):
            if step['shape'] == 'oval':
                ellipse = mpatches.Ellipse((5, step['y']), 1.5, 0.6,
                                         facecolor=step['color'],
                                         edgecolor='black', linewidth=2)
                ax.add_patch(ellipse)
            elif step['shape'] == 'diamond':
                diamond = mpatches.FancyBboxPatch((3.5, step['y']-0.4), 3, 0.8,
                                                 boxstyle="round,pad=0.1",
                                                 facecolor=step['color'],
                                                 edgecolor='black', linewidth=2)
                ax.add_patch(diamond)
            else:  # box
                box = mpatches.FancyBboxPatch((3.5, step['y']-0.3), 3, 0.6,
                                            boxstyle="round,pad=0.05",
                                            facecolor=step['color'],
                                            edgecolor='black', linewidth=1.5)
                ax.add_patch(box)
            
            ax.text(5, step['y'], step['text'], 
                   fontsize=10, ha='center', va='center', weight='bold')
        
        # Draw arrows between steps
        for i in range(len(steps)-1):
            if i == 3:  # After "Input Valid?" diamond
                # Yes arrow
                ax.arrow(5, steps[i]['y']-0.5, 0, -0.4,
                        head_width=0.2, head_length=0.1, fc='black', ec='black')
                ax.text(5.5, steps[i]['y']-0.7, 'Yes', fontsize=9)
                # No arrow (loop back)
                ax.annotate('', xy=(3.2, steps[1]['y']), xytext=(3.2, steps[i]['y']),
                           arrowprops=dict(arrowstyle='->', lw=1.5, color='red'))
                ax.text(2.8, (steps[1]['y'] + steps[i]['y'])/2, 'No', fontsize=9, color='red')
            else:
                ax.arrow(5, steps[i]['y']-0.4, 0, -0.3,
                        head_width=0.2, head_length=0.1, fc='black', ec='black')
        
        # Save figure
        filepath = self.docs_dir / "flowchart.png"
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return {"status": "success", "path": str(filepath)}
    
    def generate_data_flow_diagram(self):
        """Generate data flow visualization"""
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title
        ax.text(6, 7.5, 'Data Flow Diagram', 
                fontsize=16, weight='bold', ha='center')
        
        # Components
        components = [
            {'name': 'User Input', 'x': 1, 'y': 5, 'color': '#87CEEB'},
            {'name': 'Validation', 'x': 3, 'y': 5, 'color': '#FFD700'},
            {'name': 'ML Model', 'x': 6, 'y': 5, 'color': '#FFA07A'},
            {'name': 'Database', 'x': 9, 'y': 5, 'color': '#B0C4DE'},
            {'name': 'GUI Display', 'x': 6, 'y': 2, 'color': '#90EE90'},
            {'name': 'Training Data', 'x': 6, 'y': 6.5, 'color': '#DDA0DD'},
        ]
        
        for comp in components:
            box = mpatches.FancyBboxPatch((comp['x']-0.7, comp['y']-0.35), 1.4, 0.7,
                                         boxstyle="round,pad=0.05",
                                         facecolor=comp['color'],
                                         edgecolor='black', linewidth=2)
            ax.add_patch(box)
            ax.text(comp['x'], comp['y'], comp['name'], 
                   fontsize=10, ha='center', va='center', weight='bold')
        
        # Data flows
        flows = [
            {'from': (1.7, 5), 'to': (2.3, 5)},  # Input to Validation
            {'from': (3.7, 5), 'to': (5.3, 5)},  # Validation to ML
            {'from': (6.7, 5), 'to': (8.3, 5)},  # ML to Database
            {'from': (6, 4.65), 'to': (6, 2.35)},  # Results to Display
            {'from': (6, 6.15), 'to': (6, 5.35)},  # Training data to ML
        ]
        
        for flow in flows:
            ax.annotate('', xy=flow['to'], xytext=flow['from'],
                       arrowprops=dict(arrowstyle='->', lw=2, color='darkblue'))
        
        # Save figure
        filepath = self.docs_dir / "data_flow_diagram.png"
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return {"status": "success", "path": str(filepath)}


if __name__ == "__main__":
    gen = ArchitectureDiagramGenerator()
    
    print("Generating architecture diagram...")
    arch_result = gen.generate_architecture_diagram()
    print(f"✓ Architecture diagram: {arch_result}")
    
    print("\nGenerating flowchart...")
    flow_result = gen.generate_flowchart()
    print(f"✓ Flowchart: {flow_result}")
    
    print("\nGenerating data flow diagram...")
    data_result = gen.generate_data_flow_diagram()
    print(f"✓ Data flow diagram: {data_result}")
