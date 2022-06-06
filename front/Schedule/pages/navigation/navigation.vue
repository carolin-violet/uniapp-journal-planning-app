<template>
	<view class="navigation-layout">
		<view class="nav-bar">
			<view class="nav-title" v-for="(item, index) in navigations" :key="item.category_id" 
			:class="item.category_id === current ? 'active': ''" @click="changeNav(item.category_id)"
			>
				{{item.title}}
			</view>
		</view>
		<view class="nav-content">
			<nav-content :navContents="navigations[current-1]"></nav-content>
		</view>
	</view>
</template>

<script>
	import navContent from '../../components/navContent/navContent.vue'
	export default {
		data() {
			return {
				navigations: {},
				current: 1
			}
		},
		components: {
			navContent
		},
		methods: {
			async getNavgations() {
				let res = await this.myRequest({
					url: "/navigations"
				})
				console.log(res.data.navigations)
				this.navigations = res.data.navigations
			},
			changeNav(category_id) {
				this.current = category_id
			}
		},
		onLoad() {
			this.getNavgations()
		}
	}
</script>

<style lang="less" scoped>
	.navigation-layout{
		display: flex;
		height: 1400rpx;
		background-image: url(../../static/wallpapers/ae51f3deb48f8c54061ffcf5830511f3e2fe7fca.webp);
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: color;
		color: #FFFFFF;
		.nav-bar{
			width: 250rpx;
			height: 100%;
			background-color: rgba(100,100,100, 0.8);
			.nav-title{
				width: 100%;
				height: 150rpx;
				line-height: 150rpx;
				font-size: 30rpx;
				letter-spacing: 3rpx;
				text-align: center;
				border-bottom: 1rpx solid rgb(200,200,200);
			}
			.active{
				color: rgb(140, 209, 237);
			}
		}
		.nav-content{
			width: 500rpx;
			height: 100%;
			border-left: 4rpx solid rgb(200,200,200);
		}
	}
</style>
