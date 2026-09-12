import {
    ScatterChart,
    Scatter,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    Legend
} from "recharts";

export function ScatterChartView({ chart }) {
    const xValues = chart.data?.x || [];
    const yValues = chart.data?.y || [];
    const targetValues = chart.data?.target || [];

    if (xValues.length === 0 || yValues.length === 0) {
        return <p>No data available.</p>;
    }

    const points = xValues.map((x, index) => ({
        x,
        y: yValues[index],
        target: targetValues[index]
    }));
    const groups = targetValues.length > 0
        ? [...new Set(targetValues)].map(target => ({
            target,
            points: points.filter(point => point.target === target)
        }))
        : [{ target: chart.title, points }];
    const colors = ["#2563EB", "#E11D48", "#059669", "#D97706", "#7C3AED", "#0891B2"];

    return (
        <ResponsiveContainer width="100%" height={350}>
            <ScatterChart>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis type="number" dataKey="x" name={chart.x_axis} />
                <YAxis type="number" dataKey="y" name={chart.y_axis} />
                <Tooltip cursor={{ strokeDasharray: "3 3" }} />
                {groups.map((group, index) => (
                    <Scatter
                        key={group.target}
                        name={group.target}
                        data={group.points}
                        fill={colors[index % colors.length]}
                        isAnimationActive={false}
                    />
                ))}
                {targetValues.length > 0 && <Legend />}
            </ScatterChart>
        </ResponsiveContainer>
    );
}

export function GroupedBoxplotChart({ chart }) {
    const groups = chart.data?.groups || {};
    const categories = Object.keys(groups);

    if (categories.length === 0) {
        return <p>No grouped data available.</p>;
    }

    const validGroups = categories.map(category => {
        const values = [...(groups[category] || [])]
            .filter(value => typeof value === "number" && Number.isFinite(value))
            .sort((a, b) => a - b);

        if (values.length === 0) {
            return { category, valid: false };
        }

        const q1 = percentile(values, 0.25);
        const median = percentile(values, 0.5);
        const q3 = percentile(values, 0.75);
        const iqr = q3 - q1;
        const nonOutliers = values.filter(value => value >= q1 - 1.5 * iqr && value <= q3 + 1.5 * iqr);

        return {
            category,
            q1,
            median,
            q3,
            minimum: Math.min(...nonOutliers),
            maximum: Math.max(...nonOutliers),
            outliers: values.filter(value => value < q1 - 1.5 * iqr || value > q3 + 1.5 * iqr),
            valid: true
        };
    }).filter(item => item.valid);

    if (validGroups.length === 0) {
        return <p>No valid grouped data available.</p>;
    }

    const numericValues = categories.flatMap(category => groups[category] || [])
        .filter(value => typeof value === "number" && Number.isFinite(value));
    const globalMin = Math.min(...numericValues);
    const globalMax = Math.max(...numericValues);
    const range = globalMax - globalMin || 1;
    const width = 800;
    const height = 360;
    const leftMargin = 70;
    const rightMargin = 30;
    const topMargin = 30;
    const bottomMargin = 70;
    const plotWidth = width - leftMargin - rightMargin;
    const plotHeight = height - topMargin - bottomMargin;
    const scaleY = value => topMargin + (1 - (value - globalMin) / range) * plotHeight;
    const groupWidth = plotWidth / validGroups.length;
    const boxWidth = Math.min(groupWidth * 0.45, 70);
    const colors = ["#2563EB", "#E11D48", "#059669", "#D97706", "#7C3AED", "#0891B2"];

    return (
        <div style={{ width: "100%", overflowX: "auto" }}>
            <svg width="100%" height={height} viewBox={`0 0 ${width} ${height}`}>
                <line x1={leftMargin} y1={topMargin} x2={leftMargin} y2={height - bottomMargin} stroke="#64748B" />
                <line x1={leftMargin} y1={height - bottomMargin} x2={width - rightMargin} y2={height - bottomMargin} stroke="#64748B" />
                {validGroups.map((item, index) => {
                    const centerX = leftMargin + groupWidth * index + groupWidth / 2;
                    const color = colors[index % colors.length];
                    const q1Y = scaleY(item.q1);
                    const medianY = scaleY(item.median);
                    const q3Y = scaleY(item.q3);
                    const minimumY = scaleY(item.minimum);
                    const maximumY = scaleY(item.maximum);

                    return (
                        <g key={item.category}>
                            <line x1={centerX} y1={q1Y} x2={centerX} y2={minimumY} stroke={color} strokeWidth="2" />
                            <line x1={centerX} y1={q3Y} x2={centerX} y2={maximumY} stroke={color} strokeWidth="2" />
                            <line x1={centerX - boxWidth / 4} y1={minimumY} x2={centerX + boxWidth / 4} y2={minimumY} stroke={color} strokeWidth="2" />
                            <line x1={centerX - boxWidth / 4} y1={maximumY} x2={centerX + boxWidth / 4} y2={maximumY} stroke={color} strokeWidth="2" />
                            <rect x={centerX - boxWidth / 2} y={q3Y} width={boxWidth} height={q1Y - q3Y} fill={color} fillOpacity="0.35" stroke={color} strokeWidth="2" />
                            <line x1={centerX - boxWidth / 2} y1={medianY} x2={centerX + boxWidth / 2} y2={medianY} stroke="#111827" strokeWidth="3" />
                            {item.outliers.map((value, outlierIndex) => (
                                <circle key={outlierIndex} cx={centerX} cy={scaleY(value)} r="4" fill={color} />
                            ))}
                            <text x={centerX} y={height - bottomMargin + 25} textAnchor="middle" fontSize="12">{item.category}</text>
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function percentile(values, probability) {
    const index = (values.length - 1) * probability;
    const lower = Math.floor(index);
    const upper = Math.ceil(index);

    if (lower === upper) {
        return values[lower];
    }

    return values[lower] + (values[upper] - values[lower]) * (index - lower);
}
