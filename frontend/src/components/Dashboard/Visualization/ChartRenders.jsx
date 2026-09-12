import {
    BarChartView,
    PieChartView
} from "./BasicCharts";
import {
    ScatterChartView,
    GroupedBoxplotChart
} from "./BivariateCharts";
import {
    HistogramChart,
    BoxplotChart,
    DensityChart,
    ViolinChart
} from "./DistributionCharts";
import { HeatmapChart } from "./HeatmapChart";

const chartComponents = {
    histogram: HistogramChart,
    boxplot: BoxplotChart,
    pie: PieChartView,
    bar: BarChartView,
    scatter: ScatterChartView,
    density: DensityChart,
    violin: ViolinChart,
    heatmap: HeatmapChart,
    grouped_boxplot: GroupedBoxplotChart
};

function ChartRenderer({ chart }) {
    if (!chart) {
        return null;
    }

    const ChartComponent = chartComponents[chart.chart_type];

    if (!ChartComponent) {
        return (
            <p>
                Chart type "{chart.chart_type}"
                is not implemented yet.
            </p>
        );
    }

    return <ChartComponent chart={chart} />;
}

export default ChartRenderer;
