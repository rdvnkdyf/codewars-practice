// 'circular' adında dairesel bir nesne tanımlayın.
const circular = {
  value: "Hello World"
};

circular.self = circular;

// Bu dosya Codewars testleri için 'circular' nesnesini dışa aktarır.
if (typeof module !== 'undefined' && module.exports) {
  module.exports = circular;
}
