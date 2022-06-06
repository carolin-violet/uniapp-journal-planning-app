<template>
	<view class="article-layout" :style="{backgroundImage:'url('+baseUrl+urlList[Math.floor(Math.random()*urlList.length)]+')'}">
		<view class="article-body">
			<view class="article-head">		
				<!-- 日期 -->
				<view class="date">
					{{diary.date}}
				</view>
			</view>
			
				
				<!-- 正文内容 -->
				<view class="article-content">
					{{diary.content}}
				</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				diary: {},
				diary_id: 0,
				baseUrl: '../../static/ACG-diaryBG/',
				urlList: ['006yt1Omgy1gs8qmsf667j30rk12zal4.webp', '006yt1Omgy1gs8qmvbfejj30rk12zqgo.webp', '006yt1Omgy1gs8qmz1z6bj30rk12z15f.webp', '0327dcbbb1a043fa886ea669aec2cef7.webp', '082511737f9d4bcfaeb6d37d339fe4fc.webp', '0b141c9585774645b662be0b63315d44.webp', '103df7ad39c94715b3334b266ff1d39a.webp', '129720332b7648b6aa2d61de2f269775.webp', '225e499ecddd4457814882a85bb691d3.webp', '237e0090ac1f453780d1b41e7aaed8eb.webp', '242b97fe62b4477c8bc85a5c6a283298.webp', '347c119ed5cf4bf191c64c304bbf3173.webp', '3b49636a7b594f2b955f9c06e3d04544.webp', '462e68637e994495a3d821f30c989418.webp', '464ffe3fc417440db81ed2ff9d9b6b0f.webp', '48b966e7e2454e3aa5154b7c66c8a37b.webp', '515e5ee1e5a744e58fb2b26faa82ee0c.webp', '540c5eb2d9814ba8810b5d204945b00f.webp', '578e115471354a8b98c5e7914892826f.webp', '67056204fe1349d9b76ef62a92761faf.webp', '71a0808ca5b74994baa18f8f54b2a1dd.webp', '738979d2e6174f529a90d7015bf595a6.webp', '765d8880941740a3b2df61c569e96d12.webp', '79ea0ea5448240059de91ffec7037da8.webp', '7de0343262b746cd8f743c03081ed997.webp', '8b3c8a621a4f48d9b378a5a2e63e19a3.webp', '8bcf88a5e8e447038a2d96630b834f20.webp', '975414a2c8e94a28a6360fde93c5adc2.webp', '98370f7d39e54de1b351c1934f3a2e58.webp', '9ca64b60ad4e4a92be2add503eda96bd.webp', '9f3709afefda4852b72351276e5c1d6b.webp', 'a12792991dfa41debaa8b6e1b3d9b029.webp', 'a323d00816504e429d8b616775cfcccc.webp', 'af437561b6254c03921753fa5f355037.webp', 'bb53d0585d6643779abc14a483663b3c.webp', 'bb60565773564fe4b0c1861f16820220.webp', 'be70109e7ef945489623b019dd85f085.webp', 'beb6312358fc4a418af2bc74f6d12605.webp', 'c3c0f3bb9dff41bbbd4fb5fd91fe0809.webp', 'c7b6440757424ea9b70e0e2833edd941.webp', 'd2002f1d7cb24b7facf8a6b325aa2b0c.webp', 'd6944c8feae14bfb8aad991af34220be.webp', 'd8a12f90a174417cad4c8a8f98d2e075.webp', 'e3d9a980b1704965838a8e8c86a48e64.webp', 'e4a06b41ff20484083ddd2bf34dfac86.webp', 'e93c2abcf8f244579ca75eff6df4cf0c.webp', 'ea9964928da7407489a0a8c5ad8d523f.webp', 'ee8f0b9d5c2d4c9db8a952ef7148f403.webp', 'f269bcbe0cb1435c91bc9878e2987c4d.webp', 'f5444b9f189b4562804f63d57aeff91c.webp', 'fa42a0ce8a3846ab911f5156412b9f0d.webp', 'fceaf953615741e394fd352a7f809cc4.webp', 'feca8fd86ea64a9d8ed679e63824789a.webp', 'rBAAdmDpPKCATJvMAAZryYEjgLc447.webp', 'rBAAdmDpPLCAEUU9AAz7-2N1hfs871.webp', 'rBAAdmDpPLWAfsjCAA9HPkhwICY791.webp']
			}
		},
		methods: {
			async getArticle(article_id) {
				this.article = {}
				this.isCollected = false
				let res = await this.myRequest({
					url: "/diaries/" + this.diary_id
				})
				this.diary = res.data.diary
			}
		},
		onLoad(option) {
			this.diary_id = option.diary_id
			this.getArticle(this.diary_id)
		}
	}
</script>

<style lang="less" scoped>
	.article-layout{
		width: 100%;
		height: 100%;
		background-size: cover;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-position: center center;
		font-size: 40rpx;
		.article-body{
			height: 1400rpx;
			overflow: auto;
			background-color: rgba(250, 250, 250, 0.4);
			.article-head{
				margin: 30rpx auto;
				text-align: center;
				.title{
					font-size: 60rpx;
					height: 160rpx;
					line-height: 80rpx;
					word-wrap: break-word;
				}
				.author{
					font-size: 30rpx;
					height: 60rpx;
					line-height: 60rpx;
				}
			}
			.article-content{
				display: flex;
				flex-direction: column;
				padding: 0 20rpx;
				.paragraph{
					font-size: 30rpx;
					text-indent: 60rpx;
				}
			}
		}
	}
</style>
