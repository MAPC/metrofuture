require 'spec_helper'

describe FundingSource do

  before { @funding_source = FundingSource.new(name: "Mass.") }

  subject { @funding_source }
  
  it { should respond_to :name }

  it { should be_valid }

  describe "when name is blank" do
    before { @funding_source.name = " " }
    it { should_not be_valid }
  end

 describe "when title is too short" do
    before { @funding_source.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when title is too long" do
    before { @funding_source.name = "a" * 70 }
    it { should_not be_valid }
  end

end
