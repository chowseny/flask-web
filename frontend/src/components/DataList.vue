<template>
    <ul>
      <li v-for="item in dataList" :key="item.sysid">
        sysid: {{ item.sysid }}
      </li>
    </ul>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { getData } from '../../utils/api.js'
  
  const dataList = ref([])
  
  const fetchData = async () => {
      try {
          const response = await getData()
          dataList.value = response.data
      } catch (error) {
          console.error('Error fetching data:', error)
      }
  }
  
  onMounted(() => {
      fetchData()
  })
  </script>