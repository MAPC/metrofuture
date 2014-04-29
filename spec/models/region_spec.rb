require 'spec_helper'

describe Region do

  before { @region = Region.new(name: "Central Massachusetts", abbr: "CMRPC", rpa_name: "Central Massachusetts Regional Planning Commission") }

  subject { @region }
  
  it { should respond_to :name }
  it { should respond_to :abbr }
  it { should respond_to :rpa_name }

  it { should respond_to :municipalities }
  
  it { should be_valid }

  describe "when name is blank" do
    before { @region.name = " " }
    it { should_not be_valid }
  end

 describe "when name is too short" do
    before { @region.name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when name is too long" do
    before { @region.name = "a" * 71 }
    it { should_not be_valid }
  end

  describe "when abbr is blank" do
    before { @region.abbr = " " }
    it { should_not be_valid }
  end

 describe "when abbr is too short" do
    before { @region.abbr = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when abbr is too long" do
    before { @region.abbr = "a" * 11 }
    it { should_not be_valid }
  end

  describe "when rpa_name is blank" do
    before { @region.rpa_name = " " }
    it { should_not be_valid }
  end

 describe "when rpa_name is too short" do
    before { @region.rpa_name = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when rpa_name is too long" do
    before { @region.rpa_name = "a" * 141 }
    it { should_not be_valid }
  end

end
