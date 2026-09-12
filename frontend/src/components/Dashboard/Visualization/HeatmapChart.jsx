function getCellColor(value) {
    const intensity = Math.min(Math.abs(value), 1);

    if (value < 0) {
        return `rgb(${255 - Math.round(175 * intensity)}, ${255 - Math.round(115 * intensity)}, 255)`;
    }

    return `rgb(255, ${255 - Math.round(175 * intensity)}, ${255 - Math.round(175 * intensity)})`;
}

export function HeatmapChart({ chart }) {
    const labels = chart.data?.labels || [];
    const matrix = chart.data?.matrix || {};

    if (labels.length === 0) {
        return <p>No correlation data available.</p>;
    }

    const cellSize = 70;
    const leftMargin = 140;
    const topMargin = 100;
    const width = leftMargin + labels.length * cellSize + 40;
    const height = topMargin + labels.length * cellSize + 40;

    return (
        <div style={{ width: "100%", overflowX: "auto" }}>
            <svg width={width} height={height}>
                {labels.map((label, columnIndex) => (
                    <text
                        key={`column-${label}`}
                        x={leftMargin + columnIndex * cellSize + cellSize / 2}
                        y="80"
                        textAnchor="middle"
                        transform={`rotate(-45 ${leftMargin + columnIndex * cellSize + cellSize / 2} 80)`}
                        fontSize="12"
                    >
                        {label}
                    </text>
                ))}
                {labels.map((label, rowIndex) => (
                    <text
                        key={`row-${label}`}
                        x={leftMargin - 10}
                        y={topMargin + rowIndex * cellSize + cellSize / 2}
                        textAnchor="end"
                        dominantBaseline="middle"
                        fontSize="12"
                    >
                        {label}
                    </text>
                ))}
                {labels.map((rowLabel, rowIndex) => labels.map((columnLabel, columnIndex) => {
                    const value = matrix[rowLabel]?.[columnLabel] ?? 0;
                    const opacity = Math.min(Math.abs(value), 1);

                    return (
                        <g key={`${rowLabel}-${columnLabel}`}>
                            <rect
                                x={leftMargin + columnIndex * cellSize}
                                y={topMargin + rowIndex * cellSize}
                                width={cellSize}
                                height={cellSize}
                                fill={getCellColor(value)}
                                stroke="#CBD5E1"
                            />
                            <text
                                x={leftMargin + columnIndex * cellSize + cellSize / 2}
                                y={topMargin + rowIndex * cellSize + cellSize / 2}
                                textAnchor="middle"
                                dominantBaseline="middle"
                                fill={opacity > 0.55 ? "white" : "black"}
                                fontSize="12"
                            >
                                {Number(value).toFixed(2)}
                            </text>
                        </g>
                    );
                }))}
            </svg>
        </div>
    );
}
