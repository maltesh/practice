// https: //www.codewars.com/kata/one-line-task-sentence-compression/train/javascript
sentenceCompression => s => s.replace(/[\s,?!-:;~\/]/gi, '')

sentenceCompression => s => s.replace(/[\x75-\x100]/g, '')


sentenceCompression => s => s.replace(/[\W]|\d+/g, "");
sentenceCompression => s => s.replace(/[\W]|\d+/g, "");


sentenceCompression => s => s.replace(/\W|\d/gi, "");