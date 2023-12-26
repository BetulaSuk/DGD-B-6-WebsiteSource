<style>

.word {
  font-family:'Courier New', Courier, monospace;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}

.demo-carousel {
  background-color: azure;
  font-size: large;
}

.label {
  font-weight: bold;
  font-size: 16px;
}


</style>

<template>
  <section class="word">
      <p>This site is built with FastAPI and Vue.</p>
      <br />
  </section>

  <div style="display: flex;">
    <div style="flex: 1;"></div>
    <div style="flex: 4;">
      <br />
      <p class="label">Server CPU</p>
      <Progress :percent="this.cpu" :stroke-width="20" status="active" text-inside></Progress>
      <br />
      <p class="label">Server Disk</p>
      <Progress :percent="this.disk" :stroke-width="20" status="active" text-inside></Progress>
      <br />
      <p class="label">Server Memory</p>
      <Progress :percent="this.memory" :stroke-width="20" status="active" text-inside></Progress>
    </div>
    <div style="flex: 1;"></div>
  </div>

  <!--Added!!!!!-->
  <div style="display: flex;">
    <div ref='country' style="height: 400px; flex: 1;"></div>
    <div ref="continent" style="height: 400px; flex: 1;"></div>
  </div>
</template>
<script>

import * as echarts from "echarts";

import axios from 'axios';

export default {

  data () {
    return {
      cpu: 0,
      disk: 0,
      memory: 0
    }
  },
  methods: {
    init() {
    //第一张图
      var myChart = echarts.init(this.$refs['country']);
      //指定配置
      var option = {
        xAxis: {
          type: 'category',
          data: ['China', 'UK', 'U.S.A' ,  'France', 'Australia', 'Japan', 'Brazil', 'Canada']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [31,12,12,9,9,8,6,6],
            type: 'bar'
          }
        ]
      };
      //显示
      myChart.setOption(option);

    //第二张图
      var myChart = echarts.init(this.$refs['continent']);
      //指定配置
      var option = {
        legend: {
          top: 'bottom'
        },
        toolbox: {
          show: false,
          feature: {
            mark: { show: true },
            dataView: { show: false, readOnly: false },
            restore: { show: false },
            saveAsImage: { show: false }
          }
        },
        series: [{
          name: 'Continents',
          type: 'pie',
          radius: [50, 150],
          center: ['50%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 6
          },
          data: [
            { value: 45, name: 'Asia' },
            { value: 18, name: 'North America' },
            { value: 1, name: 'Africa' },
            { value: 10, name: 'Oceania' },
            { value: 54, name: 'Europe' },
            { value: 10, name:'South America'}
          ]
        }]
      };
      //显示
      myChart.setOption(option);
      this.getInfo();
    },
    getInfo() {
      axios.get('/server')
        .then(response => {
            //console.log(response.data);
            this.cpu = response.data.cpu_usage;
            this.memory = response.data.mem_usage;
            this.disk = response.data.disk_usage;
        });
    }
  },
  mounted() {
    this.init();
  },
}


</script>