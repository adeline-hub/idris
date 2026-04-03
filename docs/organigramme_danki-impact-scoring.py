import graphviz

def generer_danki_organigramme():
    dot = graphviz.Digraph(comment='Danki Impact Scoring', format='png')
    dot.attr(rankdir='TB', size='10,12')
    
    # Palette .danki
    c_violet = '#FF33FF'
    c_vert = '#33FFA2'
    c_charbon = '#121212'

    # Style global : Arrodi et épuré
    dot.attr('node', style='rounded,filled', fillcolor='white', penwidth='2', fontname='Helvetica')

    # Noeuds
    dot.node('A', 'START', shape='ellipse', color=c_vert)
    dot.node('B', 'Input Project Data', shape='parallelogram', color=c_charbon)
    dot.node('C', 'Calculate 8 Dimensions\n(Weighted Index)', shape='box', color=c_charbon)
    dot.node('D', 'Social Veto Check?\n(Gender/Mobility < 30)', shape='diamond', color=c_violet)
    dot.node('E', 'Cap at Amber (35-54)', shape='box', color=c_violet)
    dot.node('F', 'Regulatory Gate\n(EU Taxonomy/SFDR)', shape='box', color=c_charbon)
    dot.node('G', 'Assign Band\n(Red/Amber/Green)', shape='box', color=c_vert)
    dot.node('H', 'Output Results\n(Radar/PDF/PAI)', shape='parallelogram', color=c_charbon)
    dot.node('I', 'END', shape='ellipse', color=c_vert)

    # Flux
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E', label=' OUI ', color=c_violet)
    dot.edge('D', 'F', label=' NON ', color=c_vert)
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')

    dot.render('danki_scoring_flow', view=True)

if __name__ == '__main__':
    generer_danki_organigramme()