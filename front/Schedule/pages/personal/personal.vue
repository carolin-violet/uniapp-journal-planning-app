<template>
	<view class="profile-layout" :style="{backgroundImage: 'url('+imgUrl+')'}">
		<view class="profile-container">
			<!-- 头部分 -->
			<view class="profile-header">
				<view class="icons">
					<text class="iconfont icon-shezhi" @click="toNewPage('../setting/setting')"></text>
					<text class="iconfont icon-daohang" @click="toNewPage('../navigation/navigation')"></text>
				</view>
				<view class="info">
					<view class="info-item" id="info-avatar">
						<image :src="avatarUrl ? avatarUrl: '../../static/icons/avatar.webp'" mode=""></image>
					</view>
					<view class="info-item" id="info-base" v-if="isLogin">
						<text>{{userInfo.phone}}</text>
						<text>{{userInfo.nickName}}</text>
					</view>
					<view class="info-item" id="please-login" v-else>
						<text @click="toNewPage('../login/login')">点击登录</text>
					</view>
				</view>
			</view>
			
			<!-- 主体部分 -->
			<view class="profile-body">
				<view class="selector">
					<view class="section-title">
						<text @click="changeCurrent(0)" :class="current == 0 ? 'title-active' : '' ">计划分析</text>
					</view>
					<view class="section-title">
						<text @click="changeCurrent(1)" :class="current == 1 ? 'title-active' : '' ">笔记统计</text>
					</view>
				</view>
				<view class="main-content">
					<view class="select-item" v-show="current == 0">
						<plan-analyze></plan-analyze>
					</view>
					<view class="select-item" v-show="current == 1">
						<diary-analyze></diary-analyze>
					</view>
				</view>
			</view>
			
			<!-- 底部作者信息 -->
			<view class="author-info">
				<text>Copyright©2022</text>
				<text>Design by Carolin-zhou</text>
				<text>框架 uni-app</text>
			</view>
		</view>
	</view>
</template>

<script>
	import planAnalyze from "@/components/planAnalyze/planAnalyze.vue"
	import diaryAnalyze from "@/components/diaryAnalyze/diaryAnalyze.vue"
	
	export default {
		data() {
			return {
				current: 0,
				isLogin: false,
				userInfo: {},
				avatarUrl: "",
				imgUrl: "",
				imgPath: "../../static/vmgirls/",
				urlList: ['2018-01-15_18-39-51_106.webp', '2018-01-21_08-55-59_124.webp', '2018-05-04_14-09-42.webp', '2018-05-23_23-30-52.webp', '2018-06-19_21-04-27_2.webp', '2018-07-27_00-38-53.webp', '2019-06-13_02-25-28.webp', '2019-06-13_02-25-28_6.webp', '2021011115102034.webp', '2021011115111335.webp', '2021030314310722.webp', '2021031708381281.webp', '2021040309573363.webp', '2021053110095660.webp', '2021062918493740.webp', '2B535727-A928-4DF0-9DC7-28D2AA3BEBF1.webp', '31BC9AE5-0075-407E-9927-BA6A0C797AFE.webp', '4DBB54BF-B35B-4E8B-8D61-349B009D813F-3-scaled.webp', '58B766DB-E3EA-4B6F-8095-36766BD14E32.webp', '991_2017-03-05_21-28-27.webp', '991_2017-03-05_21-28-30.webp', '991_2017-03-05_21-28-51.webp', '991_2017-03-05_21-29-10.webp', '99b_2017-02-24_06-59-05.webp', '9av_2016-12-30_03-41-29.webp', '9b0_2016-12-24_21-52-17.webp', '9b6_2016-12-19_01-38-27.webp']
			}
		},
		components:{
			planAnalyze,
			diaryAnalyze
		},
		methods: {
			changeCurrent(currentId) {
				this.current = currentId
			},
			toNewPage(url) {
				uni.navigateTo({
					url
				})
			}
		},
		onLoad() {
			uni.getStorage({
				key: "user",
				success: (res) => {
					this.isLogin = true
					this.userInfo = JSON.parse(res.data)
				}
			})
			this.imgUrl = this.imgPath + this.urlList[Math.floor(Math.random()*this.urlList.length)]
		}
	}
</script>

<style lang="less" scoped>
	.profile-layout{
		width: 100%;
		background-position: center center;
		background-repeat: no-repeat;
		background-size: cover;
		background-attachment: fixed;
		color: #fff;
		.profile-container{
			height: 1400rpx;
			width: 100%;
			background-color: rgba(200,200,200,0.4);
			padding: 50rpx 0;
			.profile-header{
				margin: 0 auto;
				width: 700rpx;
				height: 250rpx;
				border-radius: 10rpx;
				background-image: linear-gradient(to right, rgba(0,0,255,0.2), rgba(0,250,0,0.3));
				.icons{
					display: flex;
					text{
						font-size: 50rpx;
						flex: 1;
						margin: 10rpx 20rpx;
					}
					text:nth-child(2){
						text-align: right;
					}
				}
				.info{
					width: 100%;
					height: 500rpx;
					display: flex;
					padding: 30rpx 80rpx;
					#info-avatar{
						width: 200rpx;
						height: 100rpx;
						image{
							width: 100rpx;
							height: 100rpx;
							border-radius: 50%;
							border: 1rpx solid #fff;
						}
					}
					#info-base{
						display: flex;
						flex-direction: column;
						margin-left: -40rpx;
						text{
							margin: 5rpx 0;
							height: 40rpx;
							line-height: 40rpx;
							font-size: 35rpx;
						}
					}
					#please-login{
						height: 60rpx;
						line-height: 60rpx;
						font-size: 50rpx;
						margin-left: -30rpx;
					}
				}
			}
			.profile-body{
				width: 100%;
				.selector{
					display: flex;
					.section-title{
						flex: 1;
						text-align: center;
						text{
							width: 210rpx;
							height: 60rpx;
							line-height: 60rpx;
							font-size: 40rpx;
							display: inline-block;	
						}
						.title-active{
							border-bottom: 4rpx solid rgb(140, 209, 237);
						}
					}
				}
				.main-content{
					margin: 30rpx auto;
					height: 920rpx;
				}
			}
			.author-info{
				display: flex;
				flex-direction: column;
				align-items: center;
				color: #000000;
				height: 100rpx;
			}
		}
	}
</style>
