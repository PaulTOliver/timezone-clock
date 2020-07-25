<template>
  <div>
    <div>
      Please select timezone:
      <select v-model="selected" :disabled="disabled">
        <option v-for="zone in zones" :value="zone" :key="zone">
          {{ zone.replace(/_/g, ' ') }}
        </option>
      </select>
      &emsp;
      <button v-on:click="get_time" :disabled="disabled || !selected">Get time</button>
    </div>
    <hr />
    <div>{{ statement }}</div>
  </div>
</template>

<script>
import axios from 'axios'
import config from '../../config'

export default {
  data() {
    return {
      disabled: true,
      selected: '',
      statement: '',
      zones: []
    }
  },
  mounted() {
    axios
      .get(`${config.api}/zones/`)
      .then(response => {
        this.zones = response.data
        this.disabled = false
      })
  },
  methods: {
    get_time() {
      this.disabled = true
      axios
        .get(`${config.api}/time-at/${this.selected}`)
        .then(response => {
          this.statement = `It's ${response.data.time} at ${response.data.zone.replace(/_/g, ' ')}`
          this.disabled = false
        })
    }
  }
}
</script>
