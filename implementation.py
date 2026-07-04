import numpy as np
import torch
import torch.nn.functional as F

def tensor_amplification(W, H, num_tensors=2):
    """
    Perform tensor amplification on the input graphon W and graph H.
    
    Args:
        W (torch.Tensor): A doubly nonnegative kernel (graphon) of size NxN.
        H (torch.Tensor): Adjacency matrix of the graph H of size MxM.
        num_tensors (int): Number of tensor powers to compute.
        
    Returns:
        torch.Tensor: Amplified tensor result.
    """
    assert W.ndim == 2 and W.shape[0] == W.shape[1], "W must be a square matrix."
    assert H.ndim == 2 and H.shape[0] == H.shape[1], "H must be a square matrix."
    
    # Normalize W to ensure it is doubly stochastic
    W = W / W.sum(dim=1, keepdim=True)
    
    # Compute the tensor power of W
    amplified_tensor = W.clone()
    for _ in range(num_tensors - 1):
        amplified_tensor = torch.einsum('ij,jk->ik', amplified_tensor, W)
    
    # Compute t(H, W) using the amplified tensor
    t_HW = torch.trace(torch.matrix_power(amplified_tensor, H.shape[0]))
    
    return t_HW

def spectral_transfer(W, H):
    """
    Compute the spectral transfer inequality for the given graphon W and graph H.
    
    Args:
        W (torch.Tensor): A doubly nonnegative kernel (graphon) of size NxN.
        H (torch.Tensor): Adjacency matrix of the graph H of size MxM.
        
    Returns:
        float: The spectral transfer value.
    """
    assert W.ndim == 2 and W.shape[0] == W.shape[1], "W must be a square matrix."
    assert H.ndim == 2 and H.shape[0] == H.shape[1], "H must be a square matrix."
    
    # Compute the spectral radius (largest eigenvalue) of W
    eigenvalues = torch.linalg.eigvals(W)
    spectral_radius = torch.max(eigenvalues.real)
    
    # Compute the density of W
    p_W = W.mean()
    
    # Compute the number of vertices and edges in H
    v_H = H.shape[0]
    e_H = H.sum() / 2  # Assuming undirected graph
    
    # Compute the spectral transfer inequality
    spectral_value = (spectral_radius ** (2 * e_H - v_H)) * (p_W ** (v_H - e_H))
    
    return spectral_value

if __name__ == '__main__':
    # Dummy data for testing
    N = 4  # Size of the graphon
    M = 3  # Size of the graph H
    
    # Random doubly nonnegative graphon W
    W = torch.rand(N, N)
    W = (W + W.T) / 2  # Make it symmetric
    W = F.relu(W)  # Ensure non-negativity
    
    # Random adjacency matrix for graph H
    H = torch.randint(0, 2, (M, M))
    H = torch.triu(H, diagonal=1)  # Ensure it's upper triangular
    H = H + H.T  # Make it symmetric
    
    print("Graphon W:")
    print(W)
    print("\nGraph H:")
    print(H)
    
    # Test tensor amplification
    t_HW = tensor_amplification(W, H, num_tensors=3)
    print("\nTensor Amplification t(H, W):")
    print(t_HW)
    
    # Test spectral transfer
    spectral_value = spectral_transfer(W, H)
    print("\nSpectral Transfer Value:")
    print(spectral_value)