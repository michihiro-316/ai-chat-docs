// TOC折りたたみ機能
document.addEventListener('DOMContentLoaded', function() {
  // ページ読み込み完了後に少し待ってから実行
  setTimeout(initCollapsibleToc, 100);
});

function initCollapsibleToc() {
  // 右サイドバーのTOCを取得
  const toc = document.querySelector('.md-sidebar--secondary .md-nav--secondary');
  if (!toc) return;

  // h2レベル（トップレベル）のリストアイテムを取得
  const topLevelItems = toc.querySelectorAll('.md-nav__list > .md-nav__item');

  topLevelItems.forEach(function(item) {
    const nestedList = item.querySelector('.md-nav__list');
    const link = item.querySelector(':scope > .md-nav__link');

    if (nestedList && link) {
      // 折りたたみ可能なアイテムにクラスを追加
      item.classList.add('toc-collapsible');
      item.classList.add('toc-collapsed'); // 初期状態は折りたたみ

      // トグルボタンを作成
      const toggle = document.createElement('span');
      toggle.className = 'toc-toggle';
      toggle.innerHTML = '▶';
      toggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        item.classList.toggle('toc-collapsed');
        toggle.innerHTML = item.classList.contains('toc-collapsed') ? '▶' : '▼';
      });

      // リンクの前にトグルボタンを挿入
      link.insertBefore(toggle, link.firstChild);
    }
  });
}
