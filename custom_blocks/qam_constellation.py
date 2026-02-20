from gnuradio import digital
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")   # Non-interactive backend

constellation = digital.qam.qam_constellation(16,True,'gray',True)

points = constellation.points()
points = [3+3j, 1+3j, 1+1j, 3+1j, -3+3j, -3+1j, -1+1j, -1+3j, -3-3j, -1-3j, -1-1j, -3-1j, 3-3j, 3-1j, 1-1j, 1-3j]

print(points)


# Extract real and imaginary parts
real_parts = [p.real for p in points]
imag_parts = [p.imag for p in points]

# Create figure
plt.figure(figsize=(6, 6))

# Plot points (optional markers)
plt.scatter(real_parts, imag_parts)

# Label each point with its index
for i, p in enumerate(points):
    plt.text(p.real, p.imag, str(i),
             ha='center', va='center')

# Axis formatting
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', 'box')
plt.xlabel("In-Phase (Real)")
plt.ylabel("Quadrature (Imag)")
plt.title("QAM Constellation")
plt.grid(True)

plt.savefig("qam_constellation.png", dpi=300, bbox_inches="tight")