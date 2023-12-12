<style>
*,
*::after,
*::before {
	box-sizing: border-box;
}

/*body为选择器，是添加样式的元素*/
body {
	font-family: 'Inconsolata', 'Monaco', monospace;
	overflow: hidden;
	margin: 0;
	color: #a0a2ae;
	background: #2f2829;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}

/*也可以用.开头，表示class="main-wrap"的元素*/
.main-wrap {
	position: relative;
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 100%;
	height: 100vh;
	background-color: #22295f;
	/*主页的背景图片*/
	/*修改之后好像没有区别()*/
	/*background-image: url(../img/bg.svg);*/
	background-repeat: no-repeat;
	background-position: 50% 10em;
	background-size: 75% auto;
}


/* Buttons */

.btn {
	margin: 0;
	padding: 0;
	cursor: pointer;
	border: none;
	background: none;
}

.btn:focus {
	outline: none;
}

.btn--search {
	font-size: 1.5em;
}

.btn--hidden {
	pointer-events: none;
	opacity: 0;
}


/* Reset Search Input */

.search__input {
	border: 0;
	background: transparent;
	border-radius: 0;
	/*此处有warning*/
	/*-webkit-appearance: none;*/
}

.search__input:focus {
	outline: none;
}


/* Links */


/*这个怎么没用上啊()*/
a,
.btn {
	text-decoration: none;
	color: #e01717;
	outline: none;
}

.hidden {
	position: absolute;
	overflow: hidden;
	width: 0;
	height: 0;
	pointer-events: none;
}


/* Icons */

.icon {
	display: block;
	width: 1.5em;
	height: 1.5em;
	margin: 0 auto;
	fill: currentColor;
}


/* Header */

.codrops-header {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	align-items: center;
	width: 100%;
	padding: 2.5em 2.75em 2.5em 1.5em;
	text-align: left;
}

.codrops-header__title {
	font-size: 1em;
	margin: 0;
	padding: 0 0.75em;
}

.codrops-header__side,
.search-wrap {
	margin: 0 0 0 auto;
}


/* Bottom nav */

.bottom-nav {
	position: relative;
	width: 100%;
	margin: auto 0 0 0;
	padding: 2.5em 2.75em 2.5em 2em;
}


/* Demo links */

.codrops-demos {
	font-weight: bold;
	padding: 1.25em 0;
	text-align: right;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	-webkit-touch-callout: none;
}

.codrops-demos span {
	display: inline-block;
	margin: 0 1em 0 0;
	vertical-align: bottom;
}

.codrops-demos a {
	position: relative;
	display: inline-block;
	margin: 0 0.1em;
	padding: 0 0.4em;
}

.codrops-demos a.current-demo::before {
	content: '';
	position: absolute;
	top: 50%;
	left: 50%;
	width: 2.25em;
	height: 2.25em;
	margin: -1.125em 0 0 -1.125em;
	border: 2px solid;
	border-radius: 50%;
}


/* Top Navigation Style */

.codrops-links {
	position: relative;
	display: flex;
	justify-content: center;
	text-align: center;
	white-space: nowrap;
}

.codrops-links::after {
	content: '';
	position: absolute;
	top: 15%;
	left: 50%;
	width: 2px;
	height: 70%;
	opacity: 0.1;
	background: currentColor;
	transform: rotate3d(0, 0, 1, 22.5deg);
}

.codrops-icon {
	display: inline-block;
	margin: 0.5em;
	padding: 0.5em;
}


/* Deco lines */

.decolines {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100vh;
	pointer-events: none;
}

.decoline {
	position: absolute;
	width: 1px;
	height: 100%;
	background: #ddd;
}

.decoline:first-child {
	right: 88em;
}

.decoline:nth-child(2) {
	right: 68em;
}

.decoline:nth-child(3) {
	right: 48em;
}

.decoline:nth-child(4) {
	right: 28em;
}

.decoline:nth-child(5) {
	right: 8em;
}


/* Demo colors */
/*这里是前景色和背景色！*/
.demo { color: #5c32f2; background-color: #fff; }
/*主页的背景图*/
.demo main { background-color: #fff; background-image: url(../assets/bg_original.svg); }
.demo a, .demo .btn { color: #000; }
.demo .btn--search-close { color: #5c32f2; }



@media screen and (max-width: 40em) {
	.codrops-header {
		display: block;
		padding: 4em 1em 0;
		text-align: center;
	}
	.codrops-header__side {
		margin: 0 auto;
	}
	.codrops-links {
		font-size: 0.85em;
		margin: 0 auto;
	}
	.search-wrap {
		font-size: 0.85em;
		position: absolute;
		top: 2.15em;
		right: 2em;
	}
	.bottom-nav {
		padding: 0.5em;
	}
	.codrops-demos {
		text-align: center;
	}
	.codrops-demos a {
		margin-bottom: 1em;
	}
	.codrops-demos span {
		display: block;
		margin: 0 auto 1em;
		text-align: center;
	}
}
/* Layout for search container */
.search {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	text-align: center;
}

.js .search {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}

.btn--search-close {
	font-size: 2em;
	position: absolute;
	top: 1.25em;
	right: 1.25em;
	display: none;
}

.js .btn--search-close {
	display: block;
}

.search__form {
	margin: 0 auto;
	padding: 0 1em;
}

/*输入框样式设定*/
.search__input {
	font-family: inherit;
	font-size: 7vw;
	line-height: 1;
	display: inline-block;
	box-sizing: border-box;
	width: 100%;
	max-width: 900px;
	padding: 0 0 0.1em;
	/*输入框下划线的颜色*/
	color: #080000;
	border-bottom: 6px solid;
}

.search__input::-webkit-input-placeholder {
	/* WebKit, Blink, Edge */
	color: #5c32f2;
}

.search__input::-moz-placeholder {
	opacity: 1;
	/* Mozilla Firefox 19+ */
	color: #5c32f2;
}

.search__input:-ms-input-placeholder {
	/* Internet Explorer 10-11 */
	color: #5c32f2;
}

.search__input::-webkit-search-cancel-button,
.search__input::-webkit-search-decoration {
	-webkit-appearance: none;
}

.search__input::-ms-clear {
	display: none;
}

.search__info {
	/*
	相对位置...?
	和display之间的联系还需要研究TODO
	*/
	position: relative;
	left: 30%;
	/*字体大小*/
	font-size: 120%;
	/*字体粗细*/
	font-weight: bold;
	/*
	display：布局...?
	width: 内容区域宽度
	*/
	display: block;
	width: 30%;
	/*左右距离*/
	margin: 0 auto;
	/*内边距(内容与边框的距离)*/
	padding: 0.85em 0;
	/*对齐: start, end, center, justify*/
	text-align: start;
	color: #5c32f2;
}

/* Dummy pages behind the main element that will animate like cards */
.page {
	position: relative;
	perspective: 1000px;
}

.page__single--dummy {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: #f7f7f7;
	background-repeat: no-repeat;
	background-position: 50% 50%;
	background-size: 75% auto;
}

.page__single:first-child {
	background-image: url(../assets/bg_down.svg);
}

.page__single:nth-child(2) {
	background-image: url(../assets/bg_right.svg);
}

.page__single:nth-child(3) {
	background-image: url(../assets/bg_left.svg);
}

.page__single:nth-child(4) {
	background-image: url(../assets/bg_up.svg);
}

/************************/
/* Transitions 			*/
/************************/

.js .page--move {
	pointer-events: none;
}

.js .page__single {
	transition: transform 0.7s;
	transition-timing-function: cubic-bezier(0.4, 1, 0.3, 1);
}

.page--move .page__single {
	transition-duration: 1.5s;
}

.js .page__single--dummy {
	transform: translate3d(0, 0, -600px);
}

.page--move .page__single:first-child {
	transform: translate3d(-20%, 100%, -3000px) rotate3d(0,0,1, -22deg);
	transition-duration: 1.8s;
}

.page--move .page__single:nth-child(2) {
	transform: translate3d(100%, 15%, -3500px) rotate3d(0,0,1, 30deg);
	transition-duration: 2s;
}

.page--move .page__single:nth-child(3) {
	transform: translate3d(-160%, 0%, -4500px) rotate3d(0,0,1, 10deg);
	transition-duration: 2.3s;
}

.page--move .page__single:nth-child(4) {
	transform: translate3d(-70%, -150%, -5000px) rotate3d(0,0,1, -10deg);
	transition-duration: 1.7s;
}

.page--move .page__single:nth-child(5) {
	/* main wrap */
	transform: translate3d(0, 0, -2500px) rotate3d(0,0,1, 3deg);
}

.js .search {
	pointer-events: none;
	transform-style: preserve-3d;
}

.js .search--open {
	pointer-events: auto;
}

/* Close button */
.btn--search-close {
	opacity: 0;
	transform: scale3d(0.8, 0.8, 1);
	transition: opacity 0.5s, transform 0.5s;
}

.search--open .btn--search-close {
	opacity: 1;
	transform: scale3d(1, 1, 1);
}

/* Search input */
.js .search__form {
	opacity: 0;
	transform: translate3d(0,0,600px);
}

.js .search--open .search__form {
	opacity: 1;
	transform: translate3d(0,0,0);
	transition: opacity 1.2s, transform 1.2s;
	transition-delay: 0.3s;
	transition-timing-function: cubic-bezier(0.4, 1, 0.3, 1);
}

@media screen and (max-width: 40em) {
	.btn--search-close {
		font-size: 1.25em;
	}
	.search__input {
		font-size: 2em;
		width: 100%;
	}
	.search__info {
		width: 100%;
		text-align: center;
	}
}

</style>


<template>
    <body ref="bodyRef" class="demo js">
		<!--可缩放矢量图形-->
		<svg class="hidden">
			<defs>
				<symbol id="icon-arrow" viewBox="0 0 24 24">
					<title>arrow</title>
					<polygon points="6.3,12.8 20.9,12.8 20.9,11.2 6.3,11.2 10.2,7.2 9,6 3.1,12 9,18 10.2,16.8 "/>
				</symbol>
				<symbol id="icon-drop" viewBox="0 0 24 24">
					<title>drop</title>
					<path d="M12,21c-3.6,0-6.6-3-6.6-6.6C5.4,11,10.8,4,11.4,3.2C11.6,3.1,11.8,3,12,3s0.4,0.1,0.6,0.3c0.6,0.8,6.1,7.8,6.1,11.2C18.6,18.1,15.6,21,12,21zM12,4.8c-1.8,2.4-5.2,7.4-5.2,9.6c0,2.9,2.3,5.2,5.2,5.2s5.2-2.3,5.2-5.2C17.2,12.2,13.8,7.3,12,4.8z"/><path d="M12,18.2c-0.4,0-0.7-0.3-0.7-0.7s0.3-0.7,0.7-0.7c1.3,0,2.4-1.1,2.4-2.4c0-0.4,0.3-0.7,0.7-0.7c0.4,0,0.7,0.3,0.7,0.7C15.8,16.5,14.1,18.2,12,18.2z"/>
				</symbol>
				<symbol id="icon-search" viewBox="0 0 24 24">
					<title>search</title>
					<path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
				</symbol>
				<symbol id="icon-cross" viewBox="0 0 24 24">
					<title>cross</title>
					<path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
				</symbol>
			</defs>
		</svg>
		
		<div ref="pageRef" class="page">
			<!--这几个跟点开搜索之后的背景页面有关-->
			<!--多个class之间用空格分开，CSS分别作用-->
			<div class="page__single page__single--dummy"></div>
			<div class="page__single page__single--dummy"></div>
			<div class="page__single page__single--dummy"></div>
			<div class="page__single page__single--dummy"></div>

			<main ref="mainRef" id="main_id" class="main-wrap page__single">
				<header class="codrops-header">
					<div class="search-wrap">
						<button @click="change_button" id="btn-search" class="btn btn--search"><svg class="icon icon--search"><use xlink:href="#icon-search"></use></svg></button>
					</div>
				</header>
			</main>
			
			<div ref="searchRef" class="search">
				<button @click="close_button" id="btn-search-close" class="btn btn--search-close" aria-label="Close search form"><svg class="icon icon--cross"><use xlink:href="#icon-cross"></use></svg></button>
				<!--这里一定要加上onsubmit，不然form内部的input默认回车触发提交和刷新-->
				<form ref="formRef" class="search__form" action="" onsubmit="return false;">
					<input ref="inputRef" id="test" class="search__input" name="search" type="text" placeholder="Find..." autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" >
						
					<!--没有这个隐形的button，无法触发回车判定-->
					<button @click="search_button" id="search__button" class="btn" type="submit"></button>

					<span ref="historyRef" id="history" class="search__info">History: </span>
				</form>
			</div><!-- /search -->
		</div><!-- /page -->
	</body>
</template>


<script>

import { defineComponent } from 'vue';
//import { mapActions } from 'vuex';
//import { ref } from 'vue';

export default defineComponent({
    name: 'Search',
    data() {
        return {
            form: {
                search_input: '',
            }
        };
    },
    methods: {
        change_button() {
			//替换图片
			//this.$refs.bodyRef.classList.add('js');
			//this.$refs.mainRef.style.backgroundImage = "url:require(../assets/bg_original.svg)";

			//添加新的类名
			this.$refs.pageRef.classList.add('page--move');
			this.$refs.searchRef.classList.add('search--open');
			//在指定时间(1200ms)后调用函数
			//setTimeout(function() {
				//设置焦点(搜索光标...?)
				//this.$refs.inputRef.focus();
			//}, 1200);
		},
        async search_button() {
			const searchTerm = this.$refs.inputRef.value;
			console.log(searchTerm);
			this.$refs.inputRef.value = '';

			//TODO
			const response = await fetch('/api/search', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ term: searchTerm }),
			});
			const result = await response.json();

			// Display the result or handle it as needed
			console.log(result);

			//加载历史
			//TODO
			this.$refs.historyRef.innerHTML = 'History: ';
        	history.forEach(item => {
            	const li = document.createElement('li');
            	li.textContent = item;
            	searchHistoryList.appendChild(li);
        	});
		},
        close_button() {
			//替换图片
			//this.$refs.mainRef.style.backgroundImage = "url:require(../assets/bg_main.svg)";

			//移除已经存在的类名
			this.$refs.pageRef.classList.remove('page--move');
			this.$refs.searchRef.classList.remove('search--open');
			//失去焦点
			//inputSearch.blur();
			this.$refs.inputRef.value = '';
		},

		/*...mapActions(['search']),
        async submit() {
            const Search = new FormData();
            Search.append('searchText', this.form.searchText);
            await this.search(Search);
            this.$router.push('/');
        }*/
    }
});
</script>