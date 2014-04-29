require 'spec_helper'

describe County do

  before { @county = County.new(name: "Inner Core") }

  subject { @county }
  
  it { should respond_to :name }
  it { should respond_to :fips }

  it { should respond_to :municipalities }
  
  it { should be_valid }

  describe "when name is blank" do
    before { @county.name = " " }
    it { should_not be_valid }
  end

 describe "when name is too short" do
    before { @county.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when name is too long" do
    before { @county.name = "a" * 71 }
    it { should_not be_valid }
  end

end
