import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    LineChart,
    Line
} from "recharts";

function percentile(values, probability) {
    const index = (values.length - 1) * probability;
    const lower = Math.floor(index);
    const upper = Math.ceil(index);

    if (lower === upper) {
        return values[lower];
    }

    return values[lower] +
        (values[upper] - values[lower]) *
        (index - lower);
}

export function HistogramChart({ chart }) {
    const values = chart.data?.values || [];

    if (values.length === 0) {
        return <p>No data available.</p>;
    }

    const binCount = chart.data?.bins || 20;
    const min = Math.min(...values);
    const max = Math.max(...values);
    const binWidth = (max - min) / binCount;

    if (binWidth === 0) {
        return <p>Not enough variation for histogram.</p>;
    }

    const bins = Array.from(
        { length: binCount },
        (_, index) => ({
            bin: (min + index * binWidth).toFixed(2),
            count: 0
        })
    );

    values.forEach((value) => {
        let index = Math.floor((value - min) / binWidth);
        index = Math.max(0, Math.min(index, binCount - 1));
        bins[index].count += 1;
    });

    return (
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={bins}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="bin" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" />
            </BarChart>
        </ResponsiveContainer>
    );
}

export function BoxplotChart({ chart }) {
    const values = chart.data?.values || [];

    if (values.length === 0) {
        return <p>No data available.</p>;
    }

    const sorted = [...values].sort((a, b) => a - b);
    const q1 = percentile(sorted, 0.25);
    const median = percentile(sorted, 0.5);
    const q3 = percentile(sorted, 0.75);
    const iqr = q3 - q1;
    const lowerFence = q1 - 1.5 * iqr;
    const upperFence = q3 + 1.5 * iqr;
    const nonOutliers = sorted.filter(
        value => value >= lowerFence && value <= upperFence
    );
    const minimum = Math.min(...nonOutliers);
    const maximum = Math.max(...nonOutliers);
    const outliers = sorted.filter(
        value => value < lowerFence || value > upperFence
    );
    const minValue = Math.min(...sorted);
    const maxValue = Math.max(...sorted);
    const range = maxValue - minValue || 1;
    const scaleX = value => 80 + ((value - minValue) / range) * 640;

    return (
        <div style={{ width: "100%", height: "220px" }}>
            <svg width="100%" height="220" viewBox="0 0 800 220">
                <line x1="80" y1="160" x2="720" y2="160" stroke="black" />
                <line x1={scaleX(minimum)} y1="110" x2={scaleX(q1)} y2="110" stroke="black" strokeWidth="2" />
                <line x1={scaleX(q3)} y1="110" x2={scaleX(maximum)} y2="110" stroke="black" strokeWidth="2" />
                <line x1={scaleX(minimum)} y1="90" x2={scaleX(minimum)} y2="130" stroke="black" strokeWidth="2" />
                <line x1={scaleX(maximum)} y1="90" x2={scaleX(maximum)} y2="130" stroke="black" strokeWidth="2" />
                <rect x={scaleX(q1)} y="75" width={scaleX(q3) - scaleX(q1)} height="70" fill="white" stroke="black" strokeWidth="2" />
                <line x1={scaleX(median)} y1="75" x2={scaleX(median)} y2="145" stroke="black" strokeWidth="3" />
                {outliers.map((value, index) => (
                    <circle key={index} cx={scaleX(value)} cy="110" r="4" fill="black" />
                ))}
                <text x={scaleX(minimum)} y="185" textAnchor="middle">{minimum.toFixed(2)}</text>
                <text x={scaleX(q1)} y="60" textAnchor="middle">Q1</text>
                <text x={scaleX(median)} y="60" textAnchor="middle">Median</text>
                <text x={scaleX(q3)} y="60" textAnchor="middle">Q3</text>
                <text x={scaleX(maximum)} y="185" textAnchor="middle">{maximum.toFixed(2)}</text>
            </svg>
        </div>
    );
}

export function DensityChart({ chart }) {
    const values = chart.data?.values || [];
    const sorted = [...values]
        .filter(value => typeof value === "number" && Number.isFinite(value))
        .sort((a, b) => a - b);

    if (sorted.length < 2) {
        return <p>Not enough data for density plot.</p>;
    }

    const min = sorted[0];
    const max = sorted[sorted.length - 1];

    if (min === max) {
        return <p>Not enough variation for density plot.</p>;
    }

    const mean = sorted.reduce((sum, value) => sum + value, 0) / sorted.length;
    const variance = sorted.reduce(
        (sum, value) => sum + Math.pow(value - mean, 2),
        0
    ) / sorted.length;
    const standardDeviation = Math.sqrt(variance);
    const bandwidth = 1.06 * standardDeviation * Math.pow(sorted.length, -1 / 5);

    if (!Number.isFinite(bandwidth) || bandwidth <= 0) {
        return <p>Unable to calculate density.</p>;
    }

    const gaussianKernel = u => Math.exp(-0.5 * u * u) / Math.sqrt(2 * Math.PI);
    const pointCount = 80;
    const step = (max - min) / (pointCount - 1);
    const densityData = Array.from({ length: pointCount }, (_, index) => {
        const value = min + index * step;
        const density = sorted.reduce(
            (sum, sample) => sum + gaussianKernel((value - sample) / bandwidth),
            0
        ) / (sorted.length * bandwidth);
        return { value, density };
    });

    return (
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={densityData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="value" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="density" dot={false} />
            </LineChart>
        </ResponsiveContainer>
    );
}

export function ViolinChart({ chart }) {
    const values = chart.data?.values || [];
    const sorted = [...values]
        .filter(value => typeof value === "number" && Number.isFinite(value))
        .sort((a, b) => a - b);

    if (sorted.length < 2) {
        return <p>Not enough data for violin plot.</p>;
    }

    const min = sorted[0];
    const max = sorted[sorted.length - 1];

    if (min === max) {
        return <p>Not enough variation for violin plot.</p>;
    }

    const mean = sorted.reduce((sum, value) => sum + value, 0) / sorted.length;
    const variance = sorted.reduce(
        (sum, value) => sum + Math.pow(value - mean, 2),
        0
    ) / sorted.length;
    const bandwidth = 1.06 * Math.sqrt(variance) * Math.pow(sorted.length, -1 / 5);

    if (!Number.isFinite(bandwidth) || bandwidth <= 0) {
        return <p>Unable to calculate violin density.</p>;
    }

    const gaussianKernel = u => Math.exp(-0.5 * u * u) / Math.sqrt(2 * Math.PI);
    const pointCount = 80;
    const step = (max - min) / (pointCount - 1);
    const density = [];
    let maxDensity = 0;

    for (let index = 0; index < pointCount; index += 1) {
        const value = min + index * step;
        const densityValue = sorted.reduce(
            (sum, sample) => sum + gaussianKernel((value - sample) / bandwidth),
            0
        ) / (sorted.length * bandwidth);
        density.push({ value, density: densityValue });
        maxDensity = Math.max(maxDensity, densityValue);
    }

    const centerX = 400;
    const top = 40;
    const bottom = 270;
    const chartHeight = bottom - top;
    const maxWidth = 180;
    const scaleY = value => bottom - ((value - min) / (max - min)) * chartHeight;
    const rightSide = [];
    const leftSide = [];

    density.forEach(point => {
        const y = scaleY(point.value);
        const width = (point.density / maxDensity) * maxWidth;
        rightSide.push({ x: centerX + width, y });
        leftSide.push({ x: centerX - width, y });
    });

    const path = [
        ...rightSide,
        ...[...leftSide].reverse()
    ].map((point, index) => `${index === 0 ? "M" : "L"} ${point.x} ${point.y}`).join(" ") + " Z";
    const q1 = percentile(sorted, 0.25);
    const median = percentile(sorted, 0.5);
    const q3 = percentile(sorted, 0.75);
    const violinFill = "#0F766E";
    const violinStroke = "#115E59";
    const quartileColor = "#F59E0B";
    const medianColor = "#E11D48";

    return (
        <div style={{ width: "100%", height: "320px" }}>
            <svg width="100%" height="320" viewBox="0 0 800 320">
                <line x1="400" y1={top} x2="400" y2={bottom} stroke="#64748B" strokeWidth="2" />
                <path d={path} fill={violinFill} fillOpacity="0.58" stroke={violinStroke} strokeWidth="2" />
                <line x1="350" y1={scaleY(q1)} x2="450" y2={scaleY(q1)} stroke={quartileColor} strokeWidth="2" />
                <line x1="330" y1={scaleY(median)} x2="470" y2={scaleY(median)} stroke={medianColor} strokeWidth="3" />
                <line x1="350" y1={scaleY(q3)} x2="450" y2={scaleY(q3)} stroke={quartileColor} strokeWidth="2" />
                <text x="480" y={scaleY(q1)} dominantBaseline="middle" fill={quartileColor}>Q1</text>
                <text x="480" y={scaleY(median)} dominantBaseline="middle" fill={medianColor}>Median</text>
                <text x="480" y={scaleY(q3)} dominantBaseline="middle" fill={quartileColor}>Q3</text>
                <text x="400" y="300" textAnchor="middle">{chart.x_axis}</text>
            </svg>
        </div>
    );
}
