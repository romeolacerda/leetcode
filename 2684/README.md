You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

Example 1
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:

- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
  It can be shown that it is the maximum number of moves that can be made.

Example 2
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.

###################################################################################

Esse algoritmo resolve o problema usando uma abordagem de busca em profundidade (DFS) com memoização para calcular o número máximo de movimentos possíveis em um grid. Aqui está a lógica de forma resumida:

Explanation :
This algorithm solves the problem using a Depth-First Search (DFS) with memoization to calculate the maximum number of moves possible in a grid. Here’s a summarized explanation of the logic:

1.Defining Valid Moves: Starting from each cell (row, col), you’re allowed to move to three possible positions:

(row - 1, col + 1) (diagonally up-right)
(row, col + 1) (right)
(row + 1, col + 1) (diagonally down-right)
However, the destination cell value must be greater than the current cell’s value for the move to be valid.

2.DFS Function: The dfs(r, c, grid, mem) function uses recursion to explore all valid paths starting from cell (r, c):

If the cell has already been calculated (using mem to store values), it returns the stored value.
Otherwise, it attempts the three possible moves and selects the path with the highest number of moves.
The maximum number of moves from each cell is stored in mem[r][c] to avoid redundant calculations.

3.Calculating Maximum Moves:

For each cell in the first column of the grid, it initiates a dfs call and gets the maximum number of moves that can be made from that cell.
Among all these calls, the algorithm keeps track of the maximum value.

4.Result: The highest number of moves among all possible starting cells in the first column is returned as the maximum number of moves.

Explicação em Português :

1. Definição de Movimentos Válidos: A partir de cada célula (row, col), é permitido mover-se para três posições:

(row - 1, col + 1) (diagonal para cima à direita)
(row, col + 1) (direita)
(row + 1, col + 1) (diagonal para baixo à direita)
No entanto, o valor na célula de destino deve ser maior que o valor na célula atual para que o movimento seja válido.

2. Função DFS: A função dfs(r, c, grid, mem) usa a recursão para explorar todos os caminhos válidos a partir da célula (r, c):

Se a célula já foi calculada (usando mem para armazenar os valores), retorna o valor armazenado.
Caso contrário, tenta os três movimentos possíveis e escolhe o caminho com o maior número de movimentos.
O número máximo de movimentos de cada célula é armazenado em mem[r][c] para evitar cálculos repetidos.

3.Calcular o Número Máximo de Movimentos:

Para cada célula na primeira coluna do grid, inicia uma chamada dfs e obtém o número máximo de movimentos que pode ser realizado a partir daquela célula.
Entre todas essas chamadas, o algoritmo escolhe o valor máximo.

4.Resultado: O maior número de movimentos entre todas as células iniciais possíveis na primeira coluna é retornado como o número máximo de movimentos.
