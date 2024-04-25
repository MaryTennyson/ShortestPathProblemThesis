import sys
from timeit import default_timer as timer

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
     
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph) 

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
        
        return graph
    
    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges_for_bf(self, node):
        return [(adjacent_node, value) for adjacent_node, value in self.graph.get(node, {}).items()]   

    def value(self, node1, node2):
        return self.graph[node1][node2]



def bellman_ford(graph, start_node, target_node):
    # Initialization
    distance = {node: float('inf') for node in graph.nodes}
    predecessor = {node: None for node in graph.nodes}
    distance[start_node] = 0

    # Relax edges repeatedly
    for _ in range(len(graph.nodes) - 1):
        for u in graph.nodes:
            for v, w in graph.get_outgoing_edges_for_bf(u):
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    # Check for negative cycles
    for u in graph.nodes:
        for v, w in graph.get_outgoing_edges_for_bf(u):
            if distance[u] + w < distance[v]:
                raise ValueError("Graph contains negative weight cycle")

    # Reconstruct shortest path
    path = []
    node = target_node
    while node is not None:
        path.append(node)
        node = predecessor[node]

    path.reverse()
    return path, distance[target_node]


# The algorithm in action!
nodes = [
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"AA",
"AB",
"AC",
"AD",
"AE",
"AF",
"AG",
"AH",
"AI",
"AJ",
"AK",
"AL",
"AM",
"AN",
"AO",
"AP",
"AQ",
"AR",
"AS",
"AT",
"AU",
"AV",
"AW",
"AX",
"AY",
"AZ",
"BA",
"BB",
"BC",
"BD",
"BE",
"BF",
"BG",
"BH",
"BI",
"BJ",
"BK",
"BL",
"BM",
"BN",
"BO",
"BP",
"BQ",
"BR",
"BS",
"BT",
"BU",
"BV",
"BW",
"BX",
"BY",
"BZ",
"CA",
"CB",
"CC",
"CD",
"CE",
"CF",
"CG",
"CH",
"CI",
"CJ",
"CK",
"CL",
"CM",
"CN",
"CO",
"CP",
"CQ",
"CR",
"CS",
"CT",
"CU",
"CV",
"CW",
"CX",
"CY",
"CZ",
"DA",
"DB",
"DC",
"DD",
"DE",
"DF",
"DG",
"DH",
"DI",
"DJ",
"DK",
"DL",
"DM",
"DN",
"DO",
"DP",
"DQ",
"DR",
"DS",
"DT",
"DU",
"DV",
"DW",
"DX",
"DY",
"DZ",
"EA",
"EB",
"EC",
"ED",
"EE",
"EF",
"EG",
"EH",
"EI",
"EJ",
"EK",
"EL",
"EM",
"EN",
"EO",
"EP",
"EQ",
"ER",
"ES",
"ET",
"EU",
"EV",
"EW",
"EX",
"EY",
"EZ",
"FA",
"FB",
"FC",
"FD",
"FE",
"FF",
"FG",
"FH",
"FI",
"FJ",
"FK",
"FL",
"FM",
"FN",
"FO",
"FP",
"FQ",
"FR",
"FS",
"FT",
"FU",
"FV",
"FW",
"FX",
"FY",
"FZ"
]

init_graph = { "A": {"B": 20, "C": 35, "D": 8},
"B": {"A": 20, "C": 12, "D": 42, "E": 3, "F": 29},
"C": {"A": 35, "B": 12, "D": 30, "E": 44, "F": 7},
"D": {"A": 8, "B": 42, "C": 30, "E": 18, "F": 25},
"E": {"B": 3, "C": 44, "D": 18, "F": 39, "G": 14},
"F": {"B": 29, "C": 7, "D": 25, "E": 39, "G": 32},
"G": {"E": 14, "F": 32, "H": 21, "I": 48, "J": 10},
"H": {"G": 21, "I": 46, "J": 1, "K": 47, "L": 26},
"I": {"G": 48, "H": 46, "J": 27, "K": 19, "L": 33},
"J": {"G": 10, "H": 1, "I": 27, "K": 16, "L": 22},
"K": {"H": 47, "I": 19, "J": 16, "L": 38, "M": 5},
"L": {"H": 26, "I": 33, "J": 22, "K": 38, "M": 34},
"M": {"K": 5, "L": 34, "N": 41, "O": 40, "P": 24},
"N": {"M": 41, "O": 15, "P": 43, "Q": 36, "R": 31},
"O": {"M": 40, "N": 15, "P": 11, "Q": 4, "R": 28},
"P": {"M": 24, "N": 43, "O": 11, "Q": 6, "R": 13},
"Q": {"N": 36, "O": 4, "P": 6, "R": 37, "S": 45},
"R": {"N": 31, "O": 28, "P": 13, "Q": 37, "S": 2},
"S": {"Q": 45, "R": 2, "T": 23, "U": 49, "V": 47},
"T": {"S": 23, "U": 17, "V": 9, "X": 50, "W": 32},
"U": {"S": 49, "T": 17, "V": 43, "X": 21, "W": 36},
"V": {"S": 47, "T": 9, "U": 43, "X": 8, "W": 19},
"W": {"T": 32, "U": 36, "V": 19, "X": 37, "Y": 26},
"X": {"T": 50, "U": 21, "V": 8, "W": 37, "Y": 16},
"Y": {"W": 26, "X": 16, "Z": 48, "AA": 22, "AB": 3},
"Z": {"Y": 48, "AA": 7, "AB": 34, "AC": 25, "AD": 19},
"AA": {"Y": 22, "Z": 7, "AB": 40, "AC": 1, "AD": 15},
"AB": {"Y": 3, "Z": 34, "AA": 40, "AC": 46, "AD": 27},
"AC": {"Z": 25, "AA": 1, "AB": 46, "AD": 20, "AE": 12},
"AD": {"Z": 19, "AA": 15, "AB": 27, "AC": 20, "AE": 4},
"AE": {"AC": 12, "AD": 4, "AF": 33, "AG": 38, "AH": 5},
"AF": {"AE": 33, "AG": 29, "AH": 9, "AI": 43, "AJ": 26},
"AG": {"AE": 38, "AF": 29, "AH": 46, "AI": 2, "AJ": 41},
"AH": {"AE": 5, "AF": 9, "AG": 46, "AI": 31, "AJ": 48},
"AI": {"AF": 43, "AG": 2, "AH": 31, "AJ": 47, "AK": 16},
"AJ": {"AF": 26, "AG": 41, "AH": 48, "AI": 47, "AK": 37},
"AK": {"AI": 16, "AJ": 37, "AL": 39, "AM": 13, "AN": 11},
"AL": {"AK": 39, "AM": 47, "AN": 23, "AO": 34, "AP": 20},
"AM": {"AK": 13, "AL": 47, "AN": 45, "AO": 42, "AP": 28},
"AN": {"AK": 11, "AL": 23, "AM": 45, "AO": 7, "AP": 36},
"AO": {"AL": 34, "AM": 42, "AN": 7, "AP": 32, "AQ": 18},
"AP": {"AL": 20, "AM": 28, "AN": 36, "AO": 32, "AQ": 6},
"AQ": {"AO": 18, "AP": 6, "AR": 24, "AS": 15, "AT": 31},
"AR": {"AQ": 24, "AS": 25, "AT": 37, "AU": 1, "AV": 14},
"AS": {"AQ": 15, "AR": 25, "AT": 36, "AU": 29, "AV": 41},
"AT": {"AQ": 31, "AR": 37, "AS": 36, "AU": 22, "AV": 10},
"AU": {"AR": 1, "AS": 29, "AT": 22, "AV": 45, "AW": 49},
"AV": {"AR": 14, "AS": 41, "AT": 10, "AU": 45, "AW": 38},
"AW": {"AU": 49, "AV": 38, "AX": 35, "AY": 46, "AZ": 40},
"AX": {"AW": 35, "AY": 30, "AZ": 2, "BA": 17, "BB": 28},
"AY": {"AW": 46, "AX": 30, "AZ": 37, "BA": 47, "BB": 23},
"AZ": {"AW": 40, "AX": 2, "AY": 37, "BA": 32, "BB": 8},
"BA": {"AZ": 32, "BB": 19, "BC": 43, "BD": 22, "BE": 39},
"BB": {"AZ": 8, "BA": 19, "BC": 4, "BD": 28, "BE": 5},
"BC": {"BA": 43, "BB": 4, "BD": 22, "BE": 39, "BF": 47},
"BD": {"BA": 22, "BB": 28, "BC": 22, "BE": 36, "BF": 15},
"BE": {"BA": 39, "BB": 5, "BC": 39, "BD": 36, "BF": 12},
"BF": {"BC": 47, "BD": 15, "BE": 12, "BG": 31, "BH": 5},
"BG": {"BD": 34, "BE": 23, "BF": 31, "BH": 40, "BI": 50},
"BH": {"BD": 27, "BE": 42, "BF": 5, "BG": 40, "BI": 11},
"BI": {"BG": 50, "BH": 11, "BJ": 38, "BK": 48, "BL": 9},
"BJ": {"BI": 38, "BK": 29, "BL": 24, "BM": 45, "BN": 28},
"BK": {"BI": 48, "BJ": 29, "BL": 50, "BM": 1, "BN": 44},
"BL": {"BI": 9, "BJ": 24, "BK": 50, "BM": 30, "BN": 16},
"BM": {"BJ": 45, "BK": 1, "BL": 30, "BN": 13, "BO": 33},
"BN": {"BJ": 28, "BK": 44, "BL": 16, "BM": 13, "BO": 47},
"BO": {"BM": 33, "BN": 47, "BP": 21, "BQ": 48, "BR": 34},
"BP": {"BM": 10, "BN": 38, "BO": 21, "BQ": 3, "BR": 23},
"BQ": {"BO": 48, "BP": 3, "BR": 27, "BS": 36, "BT": 47},
"BR": {"BO": 34, "BP": 23, "BQ": 27, "BS": 32, "BT": 28},
"BS": {"BQ": 36, "BR": 32, "BT": 4, "BU": 16, "BV": 46},
"BT": {"BQ": 47, "BR": 28, "BS": 4, "BU": 39, "BV": 19},
"BU": {"BS": 16, "BT": 39, "BV": 26, "BW": 48, "BX": 49},
"BV": {"BS": 46, "BT": 19, "BU": 26, "BW": 25, "BX": 38},
"BW": {"BU": 48, "BV": 25, "BX": 44, "BY": 13, "BZ": 37},
"BX": {"BU": 49, "BV": 38, "BW": 44, "BY": 29, "BZ": 42},
"BY": {"BW": 13, "BX": 29, "BZ": 20},
"BZ": {"BY": 20,"CD":13, "CZ":11, "DE":31},
"CA": {"CB": 15, "CC": 9, "CD": 22, "CE": 34, "CF": 28},
"CB": {"CA": 15, "CC": 24, "CD": 50, "CE": 29, "CF": 35},
"CC": {"CA": 9, "CB": 24, "CD": 30, "CE": 38, "CF": 17},
"CD": {"CA": 22, "CB": 50, "CC": 30, "CE": 5, "CF": 42},
"CE": {"CA": 34, "CB": 29, "CC": 38, "CD": 5, "CF": 13},
"CF": {"CA": 28, "CB": 35, "CC": 17, "CD": 42, "CE": 13},
"CG": {"CH": 8, "CI": 41, "CJ": 3, "CK": 20, "CL": 49},
"CH": {"CG": 8, "CI": 47, "CJ": 45, "CK": 32, "CL": 28},
"CI": {"CG": 41, "CH": 47, "CJ": 25, "CK": 11, "CL": 4},
"CJ": {"CG": 3, "CH": 45, "CI": 25, "CK": 14, "CL": 23},
"CK": {"CG": 20, "CH": 32, "CI": 11, "CJ": 14, "CL": 21},
"CL": {"CG": 49, "CH": 28, "CI": 4, "CJ": 23, "CK": 21},
"CM": {"CD": 15, "CO": 29, "CP": 39, "CQ": 22, "CR": 36},
"CN": {"CM": 15, "CO": 34, "CP": 23, "CQ": 31, "CR": 19},
"CO": {"CM": 29, "CN": 34, "CP": 46, "CQ": 8, "CR": 16},
"CP": {"CM": 39, "CN": 23, "CO": 46, "CQ": 37, "CR": 45},
"CQ": {"CM": 22, "CN": 31, "CO": 8, "CP": 37, "CR": 47},
"CR": {"CM": 36, "CN": 19, "CO": 16, "CP": 45, "CQ": 47},
"CS": {"CT": 10, "CU": 33, "CV": 38, "CW": 18, "CX": 4},
"CT": {"CS": 10, "CU": 42, "CV": 20, "CW": 35, "CX": 29},
"CU": {"CS": 33, "CT": 42, "CV": 17, "CW": 30, "CX": 7},
"CV": {"CS": 38, "CT": 20, "CU": 17, "CW": 46, "CX": 41},
"CW": {"CS": 18, "CT": 35, "CU": 30, "CV": 46, "CX": 21},
"CX": {"CS": 4, "CT": 29, "CU": 7, "CV": 41, "CW": 21},
"CY": {"CZ": 50, "DA": 45, "DB": 2, "DC": 13, "DD": 29},
"CZ": {"CY": 50, "DA": 28, "DB": 9, "DC": 39, "DD": 17},
"DA": {"CY": 45, "CZ": 28, "DB": 29, "DC": 16, "DD": 35},
"DB": {"CY": 2, "CZ": 9, "DA": 29, "DC": 17, "DD": 10},
"DC": {"CY": 13, "CZ": 39, "DA": 16, "DB": 17, "DD": 46},
"DD": {"CY": 29, "CZ": 17, "DA": 35, "DE": 10, "DC": 46},
"DE": {"DF": 47, "DG": 29, "DH": 5, "DI": 41, "DJ": 25},
"DF": {"DE": 47, "DG": 38, "DH": 41, "DI": 26, "DJ": 30},
"DG": {"DE": 29, "DF": 38, "DH": 15, "DI": 44, "DJ": 36},
"DH": {"DE": 5, "DF": 41, "DG": 15, "DI": 18, "DJ": 3},
"DI": {"DE": 41, "DF": 26, "DG": 44, "DH": 18, "DJ": 45},
"DJ": {"DE": 25, "DF": 30, "DG": 36, "DN": 3, "DI": 45},
"DK": {"DL": 46, "DM": 25, "DN": 36, "DO": 13, "DP": 19},
"DL": {"DK": 46, "DM": 28, "DN": 27, "DO": 24, "DP": 37},
"DM": {"DK": 25, "DL": 28, "DN": 40, "DO": 49, "DQ": 30},
"DN": {"DK": 36, "DL": 27, "DM": 40, "DO": 3, "DP": 45},
"DO": {"DK": 13, "DL": 24, "DM": 49, "DN": 3, "DP": 11},
"DP": {"DK": 19, "DL": 37, "DM": 30, "DN": 45, "DO": 11},
"DQ": {"DR": 39, "DS": 21, "DT": 5, "DU": 43, "DV": 8},
"DR": {"DQ": 39, "DS": 46, "DT": 40, "DU": 26, "DV": 18},
"DS": {"DQ": 21, "DR": 46, "DT": 14, "DU": 36, "DV": 28},
"DT": {"DQ": 5, "DR": 40, "DS": 14, "DU": 17, "DV": 42},
"DU": {"DQ": 43, "DR": 26, "DS": 36, "DT": 17, "DV": 25},
"DV": {"DQ": 8, "DR": 18, "DS": 28, "DT": 42,"DV": 25, "DX": 25},
"DW": {"DX": 43, "DY": 38, "DZ": 33, "EA":12},
"DX": {"DW": 43, "DY": 1, "DZ": 26,"EB":21},
"DY": {"DW": 38, "DX": 1, "DZ": 35},
"DZ": {"DW": 33, "DX": 26, "DY": 35,"EE":10},
"EA": {"DW":12, "EB": 15, "EC": 9, "ED": 22, "EE": 34, "EF": 28},
"EB": {"DX":21,"EA": 15, "EC": 24, "ED": 50, "EE": 29, "EF": 35},
"EC": {"EA": 9, "EB": 24, "ED": 30, "EE": 38, "EF": 17},
"ED": {"EA": 22, "EB": 50, "EC": 30, "EE": 5, "EF": 42},
"EE": {"DZ":10, "EA": 34, "EB": 29, "EC": 38, "ED": 5, "EF": 13,"EG":3},
"EF": {"EA": 28, "EB": 35, "EC": 17, "ED": 42, "EE": 13},
"EG": {"EH": 8, "EI": 41, "EJ": 3, "EK": 20, "EL": 49,"EE":3},
"EH": {"EG": 8, "EI": 47, "EJ": 45, "EK": 32, "EL": 28},
"EI": {"EG": 41, "EH": 47, "EJ": 25, "EK": 11, "EL": 4},
"EJ": {"EG": 3, "EH": 45, "EI": 25, "EK": 14, "EL": 23},
"EK": {"EG": 20, "EH": 32, "EI": 11, "EJ": 14, "EL": 21},
"EL": {"EG": 49, "EH": 28, "EI": 4, "EJ": 23, "EK": 21,"EQ":7},
"EM": {"ED": 15, "EO": 29, "EP": 39, "EQ": 22, "ER": 36},
"EN": {"EM": 15, "EO": 34, "EP": 23, "EQ": 31, "ER": 19},
"EO": {"EM": 29, "EN": 34, "EP": 46, "EQ": 8, "ER": 16},
"EP": {"EM": 39, "EN": 23, "EO": 46, "EQ": 37, "ER": 45},
"EQ": {"EM": 22, "EN": 31, "EO": 8, "EP": 37,"EL":7},
"ER": {"EM": 36, "EN": 19, "EO": 16, "EP": 45, "EV": 37},
"ES": {"ET": 10, "EU": 33, "EV": 38, "EW": 18, "EX": 4},
"ET": {"ES": 10, "EU": 42, "EV": 20, "EW": 35, "EX": 29},
"EU": {"ES": 33, "ET": 42, "EV": 17, "EW": 30, "EX": 7},
"EV": {"ES": 38, "ET": 20, "EU": 17, "EW": 46, "EX": 41,"ER":37},
"EW": {"ES": 18, "ET": 35, "EU": 30, "EV": 46, "EX": 21},
"EX": {"ES": 4, "ET": 29, "EU": 7, "EV": 41, "EW": 21, "FA":50},
"EY": {"EZ": 50, "FA": 45, "FB": 2, "FC": 13, "FD": 29},
"EZ": {"EY": 50, "FA": 28, "FB": 9, "FC": 39, "FD": 17,"FA":30},
"FA": {"EX":50,"EZ":30,"EY": 45, "EZ": 28, "FB": 29, "FC": 16, "FD": 35},
"FB": {"EY": 2, "EZ": 9, "FA": 29, "FC": 17, "FD": 10},
"FC": {"EY": 13, "EZ": 39, "FA": 16, "FB": 17},
"FD": {"EY": 29, "EZ": 17, "FA": 35, "FB": 10, "FE": 13},
"FE": {"FD": 13, "FF": 49, "FG": 16, "FH": 20, "FI": 38},
"FF": {"FD": 26, "FE": 49, "FG": 21, "FH": 38, "FI": 9},
"FG": {"FD": 35, "FE": 16, "FF": 21, "FH": 27, "FI": 36},
"FH": {"FD": 12, "FE": 20, "FF": 38, "FG": 27, "FI": 15},
"FI": {"FD": 47, "FE": 38, "FF": 9, "FG": 36, "FH": 15,"FM":34},
"FJ": {"FK": 31, "FL": 4, "FM": 37, "FN": 48, "FO": 22},
"FK": {"FJ": 31, "FL": 14, "FM": 3, "FN": 40, "FO": 32},
"FL": {"FJ": 4, "FK": 14, "FM": 44, "FN": 21, "FO": 35},
"FM": {"FJ": 37, "FK": 3, "FL": 44, "FN": 29, "FO": 16,"FI":34},
"FN": {"FJ": 48, "FK": 40, "FL": 21, "FM": 29, "FO": 15},
"FO": {"FJ": 22, "FK": 32, "FL": 35, "FM": 16, "FN": 15, "FS":23},
"FP": {"FQ": 8, "FR": 41, "FS": 26, "FT": 35, "FU": 19},
"FQ": {"FP": 8, "FR": 20, "FS": 10, "FT": 13, "FU": 28},
"FR": {"FP": 41, "FQ": 20, "FS": 41, "FT": 44, "FU": 15},
"FS": {"FO":23,"FP": 26, "FQ": 10, "FR": 41, "FT": 30, "FU": 33},
"FT": {"FP": 35, "FQ": 13, "FR": 44, "FS": 30, "FU": 42, "FW":21},
"FU": {"FP": 19, "FQ": 28, "FR": 15, "FS": 33, "FT": 42},
"FV": {"FW": 36, "FX": 21, "FY": 43, "FZ": 50},
"FW": {"FT":21,"FV": 36, "FX": 12, "FY": 11, "FZ": 25,},
"FX": {"FV": 21, "FW": 12, "FY": 31, "FZ": 7},
"FY": {"FV": 43, "FW": 11, "FX": 31, "FZ": 46},
"FZ": {"FW": 25,"FV": 50, "FW": 25, "FX": 7, "FY": 46}}



graph = Graph(nodes, init_graph)

print(len(nodes),"nodes",len(nodes)*5/2, "edges")

t0=timer()
path, distance = bellman_ford(graph, "A", "FZ")
t1=timer()

print("BF /Shortest path  {}: {}".format(distance, " -> ".join(path)))
print(t1-t0)


t0=timer()
path, distance = bellman_ford(graph, "EO", "AF")
t1=timer()
print("BF /Shortest Path {}:{}".format(distance, " -> ".join(path)))
print(t1-t0)