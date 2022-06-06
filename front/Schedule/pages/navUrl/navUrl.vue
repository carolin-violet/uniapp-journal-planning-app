<template>
	<view>
		{{url}}
	</view>
</template>

<script>
	export default {
		data() {
			return {
				url: ''
			};
		},
		onLoad(option) {
			this.url = option.url
		}
	}
</script>

<style lang="less">

</style>
