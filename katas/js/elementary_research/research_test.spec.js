var Research = require('./research.js');

describe("Research",function(){
	var research = new Research();

	it('given an empty string with no word',function(){
		var text = "";
		expect(Research.text).toEqual(" ");


	});
});