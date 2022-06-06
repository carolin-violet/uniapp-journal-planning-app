<template>
	<view class="diary-layout" :style="{backgroundImage: 'url('+imgUrl+')'}">
		<view class="diary-container">
			<!-- 头部分 -->
			<view class="diary-head">
				<view class="word">
					<text @click="changeCurrent(0)" :class="current === 0 ? 'active': '' ">我的日记</text>
				</view>
				<view class="word">
					<text @click="changeCurrent(1)" :class="current === 1 ? 'active': '' ">写日记</text>
				</view>
			</view>
			
			<!-- 主体部分 -->
			<view class="diary-body">
				<view class="diary-section" id="show-diary" v-if="current === 0">
					<show-diary :toRefresh="toRefresh"></show-diary>
				</view>
				<view class="diary-section" id="write-diary" v-if="current === 1">
					<write-diary></write-diary>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import showDiary from "@/components/showDiary/showDiary.vue"
	import writeDiary from "../../components/writeDiary/writeDiary.vue"
	
	export default {
		data() {
			return {
				current: 0,
				toRefresh: 0,
				imgUrl: '',
				imgPath: '../../static/ACG-diarymain/',
				urlList: ['11b80c8f9225432682871614add9f77b.webp', '137720003351ff419e063.webp', '137bd0000dafdc2683b7a.webp', '13818000370551b52a56e.webp', '1386400017453f57c42f1.webp', '138b600008382a66fa0d2.webp', '138d200006d1bbcf090b6.webp', '383a13842ede4a3ea9bfc97693837ff7.webp', '84b718d28dec4829bc628f668e8a30f9.webp', 'fe2d0003907f00e81f15.webp', 'fe460002b576687e28f2.webp', 'ffb700037baf36cf60d2.webp', 'ffcb00031a3358a0b054.webp']
			}
		},
		components:{
			showDiary,
			writeDiary
		},
		methods: {
			changeCurrent(currentId) {
				this.current = currentId
			}
		},
		onLoad() {
			this.imgUrl = this.imgPath + this.urlList[Math.floor(Math.random()*this.urlList.length)]
		},
		onPullDownRefresh() {
			this.toRefresh = 1
			setTimeout(() => {
				uni.stopPullDownRefresh()
				this.toRefresh = 0
			}, 3000)
		}
	}
</script>

<style lang="less" scoped>
	.diary-layout{
		width: 100%;
		background-position: center center;
		background-size: cover;
		background-repeat: no-repeat;
		background-attachment: fixed;
		color: #fff;
		.diary-container{
			background-color: rgba(0,0,0,0.5);
			.diary-head{
				display: flex;
				.word{
					flex: 1;
					text-align: center;
					text{
						height: 60rpx;
						line-height: 60rpx;
						font-size: 40rpx;
						width: 180rpx;
						display: inline-block;
					}
					.active{
						border-bottom: 4rpx solid rgb(140, 209, 237);
					}
				}
			}
			.diary-body{
				height: 1200rpx;
				.diary-section{
					height: 100%;
				}
			}
		}
	}
</style>
