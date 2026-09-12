import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Legend
} from "recharts";

export function BarChartView({ chart }) {
    const categories = chart.data?.categories || [];
    const counts = chart.data?.counts || [];

    if (categories.length === 0 || counts.length === 0) {
        return <p>No data available.</p>;
    }

    const colors = ["#2563EB", "#E11D48", "#059669", "#D97706", "#7C3AED", "#0891B2"];
    const data = categories.map((category, index) => ({
        category,
        count: counts[index] || 0
    }));

    return (
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count">
                    {data.map((entry, index) => (
                        <Cell key={`${entry.category}-${index}`} fill={colors[index % colors.length]} />
                    ))}
                </Bar>
            </BarChart>
        </ResponsiveContainer>
    );
}

export function PieChartView({ chart }) {
    const categories = chart.data?.categories || [];
    const counts = chart.data?.counts || [];
    const percentages = chart.data?.percentages || [];

    if (categories.length === 0 || counts.length === 0) {
        return <p>No data available.</p>;
    }

    const colors = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#A28DFF", "#FF6B6B"];
    const data = categories.map((category, index) => ({
        name: category,
        value: counts[index] || 0,
        percentage: percentages[index] || 0
    }));

    return (
        <ResponsiveContainer width="100%" height={350}>
            <PieChart>
                <Pie data={data} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={120} label={({ name, percentage }) => `${name}: ${percentage}%`}>
                    {data.map((entry, index) => (
                        <Cell key={`${entry.name}-${index}`} fill={colors[index % colors.length]} />
                    ))}
                </Pie>
                <Tooltip formatter={(value, name, props) => [`${value} (${props.payload.percentage}%)`, name]} />
                <Legend />
            </PieChart>
        </ResponsiveContainer>
    );
}
