import React from "react";
import {
  Chart,
  Interval,
  Coordinate,
  Legend,
  View,
  Annotation,
  getTheme,
} from "bizcharts";



const ProgrDonut = ({ data = [], content = {}, intervalConfig = {}, color = "red" }) => {
  const brandFill = getTheme().colors10[0];
  return (
    <Chart placeholder={false} height={200} padding="auto" autoFit>
      <Legend visible={false} />
      <View
        data={data}
        scale={{
          percent: {
            formatter: (val) => {
              return ((val).toFixed(2) || "0") + "%";
            },
          },
        }}
      >
        <Coordinate type="theta" innerRadius={0.75} />
        <Interval
          position="percent"
          adjust="stack"
          color={["type", [color, "#eee"]]}
          size={16}
          {...intervalConfig}
        />
        <Annotation.Text
          position={["50%", "48%"]}
          content={content.title}
          style={{
            lineHeight: "240px",
            fontSize: "12",
            fill: "#000",
            textAlign: "center",
          }}
        />
        <Annotation.Text
          position={["50%", "62%"]}
          content={content.percent}
          style={{
            lineHeight: "240px",
            fontSize: "24",
            fill: brandFill,
            textAlign: "center",
          }}
        />
      </View>
    </Chart>
  );
}
export default ProgrDonut;
